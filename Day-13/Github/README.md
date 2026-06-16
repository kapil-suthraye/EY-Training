# 🚀 FinSight AI — LLM Evaluation Pipeline with GitHub Actions

A production-style MLOps project that automates evaluation of Large Language Models (LLMs) for a credit-risk analysis use case using GitHub Actions, Groq-hosted models, pytest quality gates, and automated evaluation artifacts.

---

## 📋 Overview

This project demonstrates how to move an LLM evaluation workflow from a notebook environment into a CI/CD pipeline.

Every pull request automatically:

1. Runs LLM evaluation tests
2. Measures model quality
3. Detects hallucinations
4. Applies quality gates
5. Publishes evaluation artifacts
6. Blocks merges when quality standards are not met

---

## 🏦 FinSight AI Use Case

The system evaluates LLM performance on credit-risk assessment scenarios.

Example workflow:

```text
Developer opens PR
        ↓
GitHub Actions starts
        ↓
LLM evaluation harness runs
        ↓
Credit-risk test cases executed
        ↓
Quality metrics calculated
        ↓
Hallucination checks performed
        ↓
Quality gate applied
        ↓
✅ Merge allowed
or
❌ Build fails