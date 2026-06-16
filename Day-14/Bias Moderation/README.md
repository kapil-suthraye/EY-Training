# Bias Detection and Moderation for AI-Based Credit Approval Systems

## Overview

This project demonstrates fairness auditing and AI safety techniques for a machine learning-based credit approval system. The notebook explores how bias can enter automated decision-making systems and implements multiple methods to detect, explain, and mitigate such risks.

The project combines fairness evaluation, explainable AI, semantic moderation, and compliance reporting in a single workflow.

---

## Features

### Core Model

* Credit approval prediction using Logistic Regression
* Data preprocessing and feature encoding
* Model evaluation using accuracy metrics

### Fairness & Explainability

* SHAP feature attribution analysis
* Counterfactual fairness testing
* Bias analysis across gender and region
* Fairness visualization dashboards

### AI Moderation

* Keyword-based moderation layer
* Semantic intent classification using Hugging Face models
* Comparison with OpenAI Moderation API
* Defense-in-depth moderation strategy

### Audit Reporting

* Interactive Plotly dashboards
* Automated HTML audit report generation
* Moderation event analysis and visualization

---

## Extension Tasks

### Extension 1: SHAP Explanations

Explains which features influence loan approval or rejection decisions.

### Extension 2: Counterfactual Fairness

Tests whether changing only a protected attribute (e.g., gender) changes model decisions.

### Extension 3: Hugging Face Intent Classification

Classifies prompts into safe or potentially harmful intent categories.

### Extension 4: Moderation System Comparison

Compares keyword filtering, semantic classification, and OpenAI moderation.

### Extension 5: Audit Dashboard

Generates interactive fairness and compliance reports for auditors.

---

## Technologies Used

* Python
* Google Colab
* Pandas
* NumPy
* Scikit-learn
* SHAP
* Plotly
* Transformers (Hugging Face)
* OpenAI API (optional)

---

## Running the Notebook

1. Open the notebook in Google Colab.
2. Install required packages.
3. Run cells sequentially.
4. (Optional) Configure an OpenAI API key for moderation comparisons.
5. Review generated visualizations and audit reports.

---

## Project Goal

The objective of this project is to demonstrate responsible AI practices by combining:

* Fairness Evaluation
* Explainable AI (XAI)
* Bias Detection
* AI Safety Guardrails
* Compliance Reporting

for automated credit decision systems.

---

