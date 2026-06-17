# Counterfactual Fairness Testing with LangGraph

## Overview

This project demonstrates how to implement a **Counterfactual Fairness Test** using **LangGraph**, **Scikit-Learn**, and **Pandas**.

Counterfactual fairness evaluates whether a machine learning model's decision changes when a protected attribute (such as gender) is altered while keeping all other applicant attributes unchanged. If a model's prediction changes solely because gender is flipped, the model may exhibit bias.

The workflow is implemented as a **LangGraph state machine**, where each step of the fairness evaluation process is represented as a separate graph node.

---

## Objective

The goal of this project is to:

* Assess model fairness with respect to gender.
* Generate counterfactual samples by flipping gender values.
* Compare original and counterfactual predictions.
* Measure the percentage of decisions affected by gender changes.
* Produce an interpretable fairness report.

---

## Architecture

The workflow consists of the following LangGraph nodes:

```text
Encode Features
       │
       ▼
Create Counterfactual Dataset
       │
       ▼
Generate Predictions
       │
       ▼
Evaluate Fairness
       │
       ▼
Generate Report
       │
       ▼
      END
```

---

## Workflow Description

### 1. Encode Features

Categorical features are converted into numerical representations using LabelEncoder.

Encoded Columns:

* gender
* region
* employment_type

Output:

* Processed feature dataset (`X_orig`)

---

### 2. Create Counterfactual Dataset

A counterfactual version of the dataset is created by flipping the encoded gender value:

```python
X_cf["gender_enc"] = 1 - X_cf["gender_enc"]
```

All other attributes remain unchanged.

Output:

* Counterfactual dataset (`X_cf`)

---

### 3. Generate Predictions

Predictions are generated for:

* Original applicants
* Counterfactual applicants

The workflow uses:

* Trained classification model (`clf`)
* Feature scaler (`scaler`)

Output:

* `pred_orig`
* `pred_cf`

---

### 4. Evaluate Fairness

The workflow calculates:

```python
n_changed = (pred_orig != pred_cf).sum()
pct_changed = n_changed / total_applicants
```

This metric represents the percentage of applicants whose outcomes change when gender is flipped.

Output:

* Counterfactual fairness score

---

### 5. Generate Report

A detailed fairness report is produced including:

* Total applicants evaluated
* Number of changed decisions
* Percentage of changed decisions
* Fairness verdict
* Sample records with flipped outcomes

Verdict Logic:

```python
if pct_changed > 0.05:
    verdict = "NOT counterfactually fair"
else:
    verdict = "Approximately counterfactually fair"
```

---

## Technologies Used

* Python
* Pandas
* Scikit-Learn
* LangGraph
* LangChain Core

---

## Installation

Install required packages:

```bash
pip install pandas scikit-learn langgraph langchain-core
```

---

## Running the Workflow

Execute the graph using:

```python
result = app.invoke(
    {
        "df_orig": df,
        "clf": clf,
        "scaler": scaler,
        "feature_cols_all": all_features
    }
)
```

Access the fairness score:

```python
print(result["pct_changed"])
```

---

## Sample Output

```text
⚖️ COUNTERFACTUAL FAIRNESS TEST — Gender

Total applicants: 1000
Decision changed on flip: 34
Percentage changed: 3.40%

Verdict:
✅ Approximately counterfactually fair
```

---

## Project Structure

```text
project/
│
├── counterfactual_fairness_langgraph.ipynb
├── README.md
└── requirements.txt
```

---

## Key Learning Outcomes

* Understanding counterfactual fairness in AI systems.
* Building fairness evaluation pipelines using LangGraph.
* Applying state-based workflow orchestration to machine learning validation.
* Detecting bias in classification models.
* Generating interpretable fairness reports for responsible AI initiatives.

---

## Future Enhancements

Possible extensions include:

* Demographic Parity Evaluation
* Equal Opportunity Testing
* Equalized Odds Analysis
* SHAP-based Bias Detection
* Fairness Monitoring Dashboard
* Multi-Attribute Counterfactual Testing (Age, Race, Region, Income)
* LLM-generated Fairness Explanations

---

## Conclusion

This project demonstrates how LangGraph can be used to create modular, maintainable, and explainable fairness evaluation pipelines. By applying counterfactual analysis, organizations can identify and mitigate potential biases in machine learning systems, helping build more transparent and responsible AI solutions.
