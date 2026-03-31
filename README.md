# 📋 Task Priority Predictor

Have you ever had multiple tasks and no idea where to start?  
I built this project to solve exactly that problem.

This is a machine learning-based system that helps decide which task should be done first based on different factors like urgency, importance, and time left.

---

## 🎯 What This Project Does

The system takes details about your tasks and:

- Predicts whether a task is LOW, MEDIUM, or HIGH priority
- Assigns a score to each task
- Compares multiple tasks
- Suggests which task you should focus on first

Instead of guessing what to do, the model gives a structured recommendation.

---

## 🧠 Inputs Used

For each task, the following inputs are required:

- Urgency (1–10) → how soon it needs to be done  
- Difficulty (1–10) → how hard the task is  
- Time Left (in hours) → remaining time before deadline  
- Importance (1–10) → how important the task is  
- Past Delay (0 or 1) → whether similar tasks were delayed before  

---

## 📁 Project Structure

```
├── data/
│   └── data.csv              # Dataset used for training
│
├── model/
│   └── model.pkl             # Trained ML model
│
├── src/
│   ├── train.py              # Model training script
│   ├── predict.py            # Prediction logic
│   ├── task_advisor.py       # Multi-task decision system
│   └── batch_advisor.py      # Batch processing
│
├── demo.py                   # Demo with sample scenarios
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

Step 1: Install dependencies  
pip install -r requirements.txt

Step 2: Train the model  
python src/train.py

Step 3: Run prediction  
python src/predict.py

---

## 🔥 Multi-Task Decision System

The main upgrade in this project is the ability to handle multiple tasks at once.

You can input several tasks, and the system will:

- Predict priority for each task  
- Rank all tasks  
- Show a clear recommendation  

---

## 📝 Example

1. DSA Assignment – HIGH  
2. Database Project – MEDIUM  
3. Watch Lecture – LOW  

Recommended Task: DSA Assignment

---

## ⚙️ Model Details

- Model used: Decision Tree Classifier  
- Problem type: Supervised Learning (Classification)  
- Output classes: LOW, MEDIUM, HIGH  

The dataset was manually created to reflect real-life task scenarios.

---

## 📊 How It Works (Simple Explanation)

1. Input task details  
2. Model predicts priority  
3. Priority is converted to a score  
4. Tasks are ranked  
5. Top task is recommended  

---

## 💡 Why I Built This

I often found it difficult to decide what to do first when multiple tasks were pending.  
This project is an attempt to use machine learning to support better decision-making.

---

## 🚀 Future Improvements

- Add a UI (Streamlit or web app)  
- Improve dataset size  
- Try advanced models like Random Forest  
- Add explainability (why a task is high priority)  

---

## 📌 Notes

- Dataset is manually created for learning purposes  
- Model is simple but effective for demonstration  
- Focus is on combining ML with decision-making logic  

---

## 📄 Project Report

Detailed explanation is available in PROJECT_REPORT.md

Name - Mradul Sharma
Regestration number - 25BCE10205