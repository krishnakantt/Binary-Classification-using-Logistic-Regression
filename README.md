# Binary Classification using Logistic Regression
## 📌 Overview
This project applies Logistic Regression to predict employee attrition (whether an employee will leave the company) using an HR dataset.  
We train the model on features such as satisfaction level, last evaluation score, and average monthly hours to classify employees into two categories:  
- 0 → Stayed
- 1 → Left
The project includes data visualization, model training, evaluation, and accuracy measurement.


---

## 🛠️ Technologies Used
- Python
- Pandas – Data manipulation
- Scikit-learn – Machine learning model & evaluation
- Matplotlib / Seaborn – Data visualization

---

## 📂 Project Structure
```bash
├── HR_comma_sep.csv       # HR dataset
├── main.py                # Main script for model training & evaluation
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## ⚙️ Installation
1. Clone the repository
```bash
git clone https://github.com/krishnakantt/binary-classification-using-logistic-regression.git
cd binary-classification-using-logistic-regression
```
2. Install dependencies
```bash
pip install -r requirements.txt
```

---

## ▶️ Usage
Run the main script to train and evaluate the model:
```bash
python main.py
```

---

## 📊 Evaluation Metrics
The model is evaluated using:
- satisfaction_level – Employee job satisfaction
- last_evaluation – Performance score from last evaluation
- average_montly_hours – Average working hours per month

---

## 📈 Model Workflow
1. Data Loading – Read the HR dataset from CSV.
2. Visualization – Plot relationship between satisfaction level and attrition.
3. Preprocessing – Scale features for better model performance.
4. Model Training – Train Logistic Regression with scaled data.
5. Evaluation – Accuracy score, classification report, and confusion matrix.

---

## 📊 Example Output
- Accuracy: Displays overall model accuracy.
- Classification Report: Precision, recall, and F1-score.
- Confusion Matrix: Visual representation of predictions vs actuals.

---

## 🔮 Possible Improvements
- Use additional features (e.g., number of projects, promotion history).
- Apply hyperparameter tuning (GridSearchCV).
- Compare with other classification models (Random Forest, SVM, etc.).

---

