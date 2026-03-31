import pandas as pd
import joblib
import os
import sys

# Setup to find the training script
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from src.train import train_decision_tree, calculate_formula_score
except ImportError:
    from train import train_decision_tree, calculate_formula_score


def predict_priority(model, difficulty, time_left, importance, past_delay):
    formula_score = calculate_formula_score(difficulty, time_left, importance, past_delay)
    X = pd.DataFrame({'formula_score': [formula_score]})
    prediction = model.predict(X)[0]
    labels = {0: 'LOW', 1: 'MEDIUM', 2: 'HIGH'}
    return labels[prediction]


def get_priority_score(priority):
    scores = {'LOW': 30, 'MEDIUM': 60, 'HIGH': 90}
    return scores.get(priority, 0)


if __name__ == "__main__":
    MODEL_PATH = "models/decision_tree.pkl"
    
    if not os.path.exists(MODEL_PATH):
        print("First time? Training model...")
        train_decision_tree()
    
    model = joblib.load(MODEL_PATH)
    print("✓ Model loaded!\n")
    
    while True:
        try:
            num_tasks = int(input("How many tasks do you want to prioritize? "))
            if num_tasks <= 0:
                print("❌ Please enter a positive number!\n")
                continue
            break
        except ValueError:
            print("❌ Please enter a valid number!\n")
    
    print("\n" + "=" * 60)
    tasks = []
    
    for i in range(num_tasks):
        print(f"\n--- Task {i+1} of {num_tasks} ---")
        
        task_name = input("Task name: ").strip()
        if not task_name:
            print("❌ Task name cannot be empty!")
            continue
        
        try:
            difficulty = int(input("Difficulty (1-10): "))
            time_left = float(input("Time left (hours): "))
            importance = int(input("Importance (1-10): "))
            past_delay = int(input("Past delay (0=no, 1=yes): "))
            
            if not (1 <= difficulty <= 10 and 
                    1 <= importance <= 10 and past_delay in [0, 1]):
                print("❌ Invalid input values! Try again.\n")
                continue
            
            formula_score = calculate_formula_score(difficulty, time_left, 
                                                   importance, past_delay)
            
            priority = predict_priority(model, difficulty, time_left, 
                                       importance, past_delay)
            score = get_priority_score(priority)
            
            tasks.append({
                'name': task_name,
                'difficulty': difficulty,
                'time_left': time_left,
                'importance': importance,
                'past_delay': past_delay,
                'formula_score': formula_score,
                'priority': priority,
                'score': score
            })
            
        except ValueError:
            print("❌ Invalid input! Please try again.\n")
            continue
    
    tasks_sorted = sorted(tasks, key=lambda x: x['score'], reverse=True)
    
    print("\n" + "=" * 60)
    print("TASK PRIORITY RANKING")
    print("=" * 60 + "\n")
    
    for rank, task in enumerate(tasks_sorted, 1):
        print(f"{rank}. {task['name']} -- {task['priority']} (Score: {task['score']}/90)")
        print(f"   Difficulty: {task['difficulty']}/10 | Importance: {task['importance']}/10 | Time: {task['time_left']}h")
        print(f"   Formula Score: {task['formula_score']}/100")
        print()
    
    if tasks_sorted:
        top_task = tasks_sorted[0]
        print("=" * 60)
        print(f">>> RECOMMENDED TASK: {top_task['name'].upper()} <<<")
        print(f"Priority: {top_task['priority']} | Score: {top_task['score']}/90")
        print("=" * 60)
