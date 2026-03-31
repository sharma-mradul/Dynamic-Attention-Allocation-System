# 📘 Project Report  
## Dynamic Attention Allocation System

---

## 1. Introduction

In daily life, students and professionals often face situations where multiple tasks need to be completed within limited time. Deciding which task to prioritize becomes difficult, especially when each task has different levels of urgency, importance, and complexity. Poor prioritization can lead to missed deadlines and reduced productivity.

This project aims to address this problem by developing a system that helps users decide which task to focus on first using machine learning.

---

## 2. Problem Statement

The main problem addressed in this project is task prioritization. When multiple tasks are available, users often rely on intuition or incomplete judgment to decide what to do next. This approach is not always efficient and can result in poor decision-making.

The objective is to build a system that can analyze different task-related factors and predict the priority level of each task, helping users make better decisions.

---

## 3. Objective

The key objectives of this project are:

- To develop a machine learning model that predicts task priority  
- To consider multiple factors such as urgency, importance, difficulty, and time constraints  
- To extend the system to handle multiple tasks at once  
- To rank tasks and recommend which one should be done first  

---

## 4. Dataset Description

The dataset used in this project is manually created to simulate real-world task scenarios. Each entry represents a task with several features.

### Input Features:
- **Urgency (1–10):** Indicates how urgent the task is  
- **Difficulty (1–10):** Represents how complex the task is  
- **Time Left (hours):** Remaining time before deadline  
- **Importance (1–10):** Significance of the task  
- **Past Delay (0/1):** Whether similar tasks were delayed before  

### Output:
- **Priority:** LOW, MEDIUM, or HIGH  

The dataset is designed based on practical reasoning of how people usually prioritize tasks.

---

## 5. Methodology

The project follows a supervised machine learning approach.

### Steps involved:

1. **Data Collection:**  
   A custom dataset was created manually with realistic task examples.

2. **Data Preprocessing:**  
   The priority labels were converted into numerical values for model training.

3. **Model Selection:**  
   A Decision Tree Classifier was chosen due to its simplicity and interpretability.

4. **Model Training:**  
   The dataset was split into training and testing sets, and the model was trained on the training data.

5. **Prediction:**  
   The trained model predicts the priority level based on input features.

6. **Task Ranking:**  
   For multiple tasks, predicted priorities are converted into scores and tasks are ranked accordingly.

---

## 6. System Design

The system is divided into multiple components:

- **Input Module:** Takes task details from the user  
- **Prediction Module:** Uses the trained model to predict priority  
- **Ranking Module:** Sorts tasks based on predicted priority  
- **Output Module:** Displays ranked tasks and recommended task  

---

## 7. Results

The model is able to classify tasks into LOW, MEDIUM, and HIGH priority based on input features. When multiple tasks are provided, the system successfully ranks them and identifies the most important task.

The results demonstrate that even a simple machine learning model can assist in improving decision-making.

---

## 8. Advantages

- Helps in better task prioritization  
- Reduces decision-making confusion  
- Easy to use and understand  
- Can handle multiple tasks at once  

---

## 9. Limitations

- Dataset is manually created and limited in size  
- Model performance depends on input quality  
- Does not consider external factors like user mood or interruptions  

---

## 10. Future Scope

- Use larger and real-world datasets  
- Implement advanced models like Random Forest  
- Add a graphical user interface (GUI)  
- Integrate with mobile or web applications  
- Include explainable AI features  

---

## 11. Conclusion

This project demonstrates how machine learning can be applied to solve a simple but important real-life problem. By analyzing task-related features, the system can predict priority and help users decide what to focus on. The project combines machine learning with logical decision-making to create a practical and useful tool.

---

## 12. Technologies Used

- Python  
- Pandas  
- Scikit-learn  
- Joblib  

---