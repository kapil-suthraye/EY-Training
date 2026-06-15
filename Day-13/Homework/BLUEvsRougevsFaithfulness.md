# Latency Variation Analysis Using RAG Evaluation Metrics

## Relationship Between Latency and Evaluation Metrics

The latency variation observed across queries can be correlated with RAG quality metrics such as BLEU, ROUGE, and Faithfulness.

---

## 1. BLEU Score Impact

BLEU measures the overlap between generated responses and reference answers.

### Observation
Queries with higher latency may indicate:
- Longer generated responses
- More detailed explanations
- Higher token generation counts

### Expected Trend
| BLEU Score | Expected Latency |
|------------|-----------------|
| Low | Lower |
| Medium | Moderate |
| High | Higher |

### Reason
To achieve higher BLEU scores, the model often generates more complete and precise responses, increasing generation time.

---

## 2. ROUGE Score Impact

ROUGE measures content coverage and recall against reference answers.

### Observation
Queries requiring extensive context utilization generally:
- Produce longer outputs
- Include more retrieved information
- Increase inference time

### Expected Trend
| ROUGE Score | Expected Latency |
|-------------|-----------------|
| Low | Lower |
| Medium | Moderate |
| High | Higher |

### Reason
Higher ROUGE scores typically indicate broader coverage of retrieved documents, resulting in additional generation latency.

---

## 3. Faithfulness Impact

Faithfulness measures how well the answer is grounded in retrieved context and whether hallucinations are avoided.

### Observation
Highly faithful responses often require:
- Processing larger retrieved contexts
- Cross-checking multiple chunks
- More reasoning steps

### Expected Trend
| Faithfulness | Expected Latency |
|-------------|-----------------|
| Low | Lower |
| Medium | Moderate |
| High | Higher |

### Reason
Generating a grounded response generally requires additional context processing, increasing LLM inference time.

---

## Interpretation of Current Waterfall Chart

### Stable Stages
- Query Embedding
- Azure Retrieval

These stages show little variation and therefore have minimal impact on BLEU, ROUGE, or Faithfulness.

### Variable Stage
- Groq Generation

The generation stage contributes almost all latency variation.

This suggests that differences in:
- Response length
- Context utilization
- Reasoning complexity

are responsible for changes in BLEU, ROUGE, and Faithfulness scores.

---

## Possible Correlation

| Query Type | BLEU | ROUGE | Faithfulness | Expected Latency |
|------------|------|--------|--------------|------------------|
| Simple Fact Retrieval | High | Low-Medium | High | Low |
| Short Definition | Medium | Medium | High | Low |
| Summarization | High | High | High | Medium |
| Multi-hop Reasoning | High | High | High | High |
| Large Context Synthesis | High | Very High | High | Very High |

---

## Conclusion

The observed latency variation is primarily driven by the Groq generation stage. Queries achieving higher BLEU, ROUGE, and Faithfulness scores generally require:

- More retrieved context
- More reasoning
- Longer responses
- Additional token generation

As a result, higher-quality answers often incur higher generation latency, while embedding and retrieval stages remain largely unaffected.