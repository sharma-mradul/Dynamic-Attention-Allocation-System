# 📋 Task Priority Predictor

Ever get stuck deciding which task to do first? This ML project helps you figure that out! 

## 🎯 What It Does

Enter details about your tasks (like how hard they are, how important, and how much time you have), and the system will:
- **Calculates a priority score** using a formula
- **Uses machine learning** to predict if it's LOW, MEDIUM, or HIGH priority
- **Ranks all your tasks** from most to least important
- **Shows you what to work on first!**

Just give it:
- How hard is the task? (1-10)
- How much time do you have? (in hours)
- How important is it? (1-10)
- Did you delay this task before? (yes/no)

## 📁 What's Inside

```
├── data/
│   └── tasks.csv              # Example training data (500 tasks)
│
├── models/
│   └── decision_tree.pkl      # The trained AI model
│
├── src/
│   ├── train.py               # Trains the ML model
│   └── predict.py             # Predicts your task priorities
│
└── requirements.txt
```

## 🚀 Quick Start

**Step 1: Install stuff**
```bash
pip install -r requirements.txt
```

**Step 2: Train the model (one time)**
```bash
python src/train.py
```

**Step 3: Use it!**
```bash
python src/predict.py
```

## 📝 Example

```
How many tasks? 3

Task 1: Study
  Difficulty? 8
  Time left (hours)? 2
  Importance? 9
  Delayed before? 1

Task 2: Exercise  
  Difficulty? 3
  Time left (hours)? 1
  Importance? 5
  Delayed before? 0

--- RESULTS ---

1. Study - HIGH
2. Exercise - MEDIUM

✓ Do this first: Study
```

## 📦 What You Need

- pandas (for handling data)
- scikit-learn (the ML library)
- joblib (to save/load the model)

## Features

- **Multi-task support**: Handle 3-10 tasks simultaneously
- **ML-powered predictions**: Uses trained Random Forest classifier
- **Feature engineering**: Creates 9 derived features from 5 input attributes
- **Explainable AI**: Generates human-readable explanations
- **Ranked recommendations**: Intelligent sorting based on multiple factors
- **Actionable insights**: Specific next steps for each priority level

## Requirements

- Python 3.8+
- scikit-learn 1.3.2+
- pandas 2.0.3+
- numpy 1.24.3+
- joblib 1.3.1+

See LICENSE file for details.

### Train only

```bash
python src/train.py --data data/data.csv --model model/model.pkl --rebuild
```

### Prediction

#### Single input (interactive fallback)

```bash
python src/predict.py --mode single
```

or values with flags:

```bash
python src/predict.py --mode single --urgency 8 --difficulty 5 --time_left 10 --importance 9 --past_delay 1
```

#### Batch input

```bash
python src/predict.py --mode batch --input data/data.csv --output data/results.csv
```

## Key details

- Base features: `urgency`, `difficulty`, `time_left`, `importance`, `past_delay`
- Derived features: `risk`, `stress`, `urgency_adjusted`, `time_pressure`
- Model: `RandomForestClassifier` with balanced class weights

## What is in `data/` and `model/`

- `data/data.csv`: contains task samples and ground truth priorities (generated if absent)
- `model/model.pkl`: saved trained model (produced by `train.py`)

## Suggested enhancements

- Add unit/integration tests (`tests/`)
- Add GitHub Actions CI for `pytest`
- Add model explainability (e.g., SHAP)
- Add `pyproject.toml` for packaging

## 🎯 NEW: Multi-Task Decision Making Assistant

The system now includes an **advanced decision-making assistant** that handles multiple tasks with intelligent prioritization, ranking, and recommendations.

### Features

✅ **Multi-Task Input** - Accept 3-10 tasks interactively or via batch processing
✅ **Intelligent Ranking** - Rank tasks by predicted priority + additional factors
✅ **Smart Explanations** - Auto-generated explanations for each prediction
✅ **Formatted Output** - Clean, professional terminal display with visual indicators
✅ **Batch Processing** - Load from CSV or JSON files
✅ **Comparison Insights** - Shows why one task ranks higher than another
✅ **Action Recommendations** - Clear next steps with reasoning

### Quick Start

**Interactive Mode:**
```bash
python src/task_advisor.py
```

**Batch Processing (Sample):**
```bash
python src/batch_advisor.py --mode sample
```

**Demo with 3 Scenarios:**
```bash
python demo.py
```

**From CSV:**
```bash
python src/batch_advisor.py --mode csv --input data/sample_tasks.csv
```

**From JSON:**
```bash
python src/batch_advisor.py --mode json --input data/sample_tasks.json --output-csv results.csv
```

### Example Output

```
📋 RANKED TASKS:

1. DSA Assignment – HIGH (Score: 90)
   Normalized Score: 100/100
   📊 Urgency: 9/10 | Difficulty: 8/10 | Importance: 9/10 | Time Left: 2.0h
   💡 High urgency (9/10) | High importance (9/10) | Very limited time (2.0 hours) | Previously delayed

2. Database Project – MEDIUM (Score: 60)
   Normalized Score: 66/100
   📊 Urgency: 7/10 | Difficulty: 6/10 | Importance: 8/10 | Time Left: 5.0h
   💡 High urgency (7/10) | High importance (8/10)

3. Watch Lecture – LOW (Score: 30)
   Normalized Score: 33/100
   📊 Urgency: 3/10 | Difficulty: 2/10 | Importance: 5/10 | Time Left: 24.0h
   💡 Low urgency (3/10) | Plenty of time available (24.0 hours)

✅ RECOMMENDED TASK: DSA ASSIGNMENT
Priority: HIGH | Score: 90/90 | Normalized: 100/100
```

### New Modules

- **`src/task_advisor.py`** - Main interactive assistant for multi-task prioritization
- **`src/batch_advisor.py`** - Batch processing for CSV/JSON inputs
- **`demo.py`** - Interactive demonstration with 3 real-world scenarios
- **`USAGE_GUIDE.md`** - Complete documentation and examples

### Input Format

Tasks require these attributes:
- `task_name` - Name of the task
- `urgency` - 1-10 scale (10 = most urgent)
- `difficulty` - 1-10 scale (10 = hardest)
- `time_left` - Hours until deadline
- `importance` - 1-10 scale (10 = most important)
- `past_delay` - 0 or 1 (previously delayed?)

See `data/sample_tasks.csv` and `data/sample_tasks.json` for examples.

### How It Works

1. **Load Model** - Uses trained Random Forest from `model/model.pkl`
2. **Predict** - Predicts priority (LOW/MEDIUM/HIGH) for each task
3. **Score** - Converts priority to numerical score (LOW=30, MEDIUM=60, HIGH=90)
4. **Rank** - Sorts tasks by score, importance, urgency
5. **Explain** - Generates reasons for each prediction
6. **Recommend** - Highlights top task and provides next steps

## Project report

See `PROJECT_REPORT.md` for the latest summary of what was done and why.
