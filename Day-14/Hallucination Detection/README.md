# Hallucination Detection Techniques in LLM Outputs

## Overview

This Colab notebook demonstrates several practical approaches for detecting hallucinations in Large Language Model (LLM) responses. It provides hands-on examples using semantic similarity, consistency checking, factual verification, and specialized hallucination-evaluation models.

## Techniques Covered

### 1. BERTScore
Uses transformer-based contextual embeddings to compare a generated answer against a trusted reference answer.

**Purpose**
- Measure semantic similarity
- Detect deviations from known ground truth
- Flag potentially hallucinated content

**Library**
- `bert-score`

### 2. SelfCheckGPT
Generates or compares multiple responses and measures their agreement using embedding similarity.

**Purpose**
- Evaluate response consistency
- Identify unstable or contradictory generations
- Estimate confidence without external knowledge sources

**Libraries**
- `sentence-transformers`
- `scikit-learn`

### 3. FactScore-Style Verification
Compares extracted claims against supporting evidence using semantic embeddings.

**Purpose**
- Verify factual grounding
- Measure claim-evidence alignment
- Detect unsupported statements

**Libraries**
- `sentence-transformers`

### 4. HHEM (Hallucination Evaluation Model)
Demonstrates the use of Vectara's hallucination evaluation model available through Hugging Face.

**Purpose**
- Specialized hallucination assessment
- Entailment-style verification
- Automated factual consistency scoring

**Libraries**
- `transformers`
- `sentencepiece`
- `tokenizers`

---

## Installation

```bash
pip install transformers torch sentence-transformers bert-score
pip install openai
pip install requests
```

Additional dependencies for the Vectara model:

```bash
pip install sentencepiece tiktoken
```

## Notebook Structure

1. Library installation
2. BERTScore example and interpretation
3. SelfCheckGPT consistency scoring
4. FactScore-style claim verification
5. Vectara HHEM setup and evaluation
6. Example comparisons of factual and hallucinated statements

## Example Use Cases

- Evaluating LLM-generated answers
- Building RAG evaluation pipelines
- Detecting factual inconsistencies
- Benchmarking model reliability
- Research and educational demonstrations

## Interpretation Guidelines

### BERTScore
| Score | Interpretation |
|---------|---------------|
| > 0.90 | Very similar |
| 0.80–0.90 | Mostly correct |
| < 0.80 | Potential hallucination |

### SelfCheckGPT Similarity
| Score | Interpretation |
|---------|---------------|
| > 0.90 | Very consistent |
| 0.75–0.90 | Moderate confidence |
| < 0.75 | Likely hallucination |

### FactScore-Style Verification
| Score | Interpretation |
|---------|---------------|
| 0.90–1.00 | Excellent factual grounding |
| 0.75–0.90 | Mostly factual |
| 0.50–0.75 | Significant factual issues |
| < 0.50 | Many hallucinations |

## Notes

- The notebook uses simple illustrative examples centered on factual statements about Paris.
- Similarity-based approaches do not guarantee factual correctness.
- Retrieval-augmented verification generally provides stronger hallucination detection than reference-free methods.
- Production systems often combine multiple techniques for improved reliability.

## License

Use and modify this notebook for educational, research, and experimentation purposes.
