import os
import joblib
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


def calculate_formula_score(difficulty, time_left, importance, past_delay):
    score = (importance * 3) + (difficulty * 2) + (100 / time_left) + (past_delay * 25)
    normalized_score = min(100, (score / 50) * 100)
    return round(normalized_score, 2)


def create_sample_data(file_path="data/tasks.csv"):
    np.random.seed(42)
    
    n_samples = 500
    difficulties = np.random.randint(1, 11, n_samples)
    time_lefts = np.random.uniform(0.5, 96, n_samples)
    importances = np.random.randint(1, 11, n_samples)
    past_delays = np.random.randint(0, 2, n_samples)
    
    priorities = []
    for difficulty, time_left, importance, past_delay in zip(difficulties, time_lefts, importances, past_delays):
        score = (importance * 3) + (difficulty * 2) + (100 / time_left) + (past_delay * 25)
        if score > 120:
            priorities.append('HIGH')
        elif score > 70:
            priorities.append('MEDIUM')
        else:
            priorities.append('LOW')
    
    data = {
        'difficulty': difficulties,
        'time_left': time_lefts,
        'importance': importances,
        'past_delay': past_delays,
        'priority': priorities
    }
    
    df = pd.DataFrame(data)
    
    df['formula_score'] = df.apply(
        lambda row: calculate_formula_score(row['difficulty'], row['time_left'], 
                                           row['importance'], row['past_delay']),
        axis=1
    )
    
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    df.to_csv(file_path, index=False)
    
    print(f"✓ Generated {n_samples} training samples")


def train_decision_tree(data_path="data/tasks.csv", model_path="models/decision_tree.pkl"):
    if not os.path.exists(data_path):
        create_sample_data(data_path)
    
    data = pd.read_csv(data_path)
    
    if 'formula_score' not in data.columns:
        data['formula_score'] = data.apply(
            lambda row: calculate_formula_score(row['difficulty'], row['time_left'], 
                                               row['importance'], row['past_delay']),
            axis=1
        )
    
    X = data[['formula_score']]
    y = data['priority']
    
    priority_map = {'LOW': 0, 'MEDIUM': 1, 'HIGH': 2}
    y = y.map(priority_map)
    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    model = DecisionTreeClassifier(random_state=42, max_depth=5)
    model.fit(X_train, y_train)
    
    accuracy = accuracy_score(y_test, model.predict(X_test))
    print(f"Model Accuracy: {accuracy:.2%}")
    
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    print(f"✓ Model saved to {model_path}")


if __name__ == "__main__":
    train_decision_tree()
