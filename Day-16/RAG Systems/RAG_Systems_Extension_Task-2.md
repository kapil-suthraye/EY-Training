# Chunking Strategy Latency Analysis

## Experiment Results

### Chunk Size Comparison

| Chunk Size | Number of Chunks | Average Latency (s) |
| ---------- | ---------------- | ------------------- |
| 256        | 13               | 1.43                |
| 512        | 7                | 1.84                |
| 1024       | 4                | 1.86                |

---

## Chunk Size = 256

### Observations

* Highest number of chunks generated (**13 chunks**)
* Lowest average latency (**1.43 seconds**)

### Why?

Although more chunks are created, each chunk contains significantly less text.

### Retrieval Flow

```text
Query
  ↓
Vector Search
  ↓
Top-K Retrieved Chunks
  ↓
LLM Response Generation
```

Since the retrieved chunks are smaller:

* Less context is passed to the LLM
* Fewer prompt tokens are processed
* Faster inference time

### Impact

#### Pros

* Fastest response time
* Lower token consumption
* Reduced LLM cost

#### Cons

* Context fragmentation
* Important financial or business information may be split across multiple chunks
* Increased risk of incomplete answers

---

## Chunk Size = 512

### Observations

* Generated **7 chunks**
* Average latency increased to **1.84 seconds**

### Why?

Each chunk contains approximately twice the content compared to a chunk size of 256.

As a result:

* More tokens are sent to GPT-4o
* Context processing time increases
* Prompt construction becomes larger

### Impact

#### Pros

* Better context continuity
* Improved retrieval quality
* Reduced fragmentation

#### Cons

* Higher latency
* Increased token usage
* Higher inference cost

---

## Chunk Size = 1024

### Observations

* Generated only **4 chunks**
* Highest latency observed (**1.86 seconds**)

### Why?

Although fewer vectors need to be searched, each retrieved chunk is substantially larger.

In most RAG systems, latency is dominated by:

**LLM Generation Time**

rather than:

**Vector Similarity Search Time**

Large chunks increase:

* Prompt size
* Input token count
* Context processing overhead

These factors offset any retrieval gains achieved by having fewer vectors.

### Impact

#### Pros

* Maximum contextual information
* Lower probability of missing related content
* Strong context preservation

#### Cons

* Highest latency
* More irrelevant information may be included
* Increased token consumption and cost

---

# Why Did Smaller Chunks Perform Faster?

A common assumption is:

> More Chunks = Higher Latency

However, the experiment demonstrates the opposite.

### Key Reason

The dominant contributor to latency is:

**LLM Processing Time**

not

**FAISS Vector Search Time**

Comparing searches across:

* 13 vectors (chunk size 256)
* 7 vectors (chunk size 512)
* 4 vectors (chunk size 1024)

results in only a negligible difference in FAISS search latency.

The major factor is:

## Number of Tokens Sent to GPT-4o

Smaller chunks produce:

* Smaller prompts
* Fewer input tokens
* Faster context processing
* Faster response generation

Therefore, despite creating more chunks, the **256 chunk size achieved the lowest overall latency**.

---

# Summary

| Chunk Size | Retrieval Quality | Context Continuity | Token Cost | Latency  |
| ---------- | ----------------- | ------------------ | ---------- | -------- |
| 256        | Medium            | Low                | Low        | Best     |
| 512        | High              | Medium             | Medium     | Moderate |
| 1024       | Very High         | High               | High       | Worst    |

## Recommended Choice

### For Latency-Sensitive Applications

Use **Chunk Size = 256**

* Fastest responses
* Lowest token usage
* Lowest operational cost

### For Balanced Performance

Use **Chunk Size = 512**

* Better context preservation
* Improved retrieval quality
* Reasonable latency trade-off

### For Maximum Context Retention

Use **Chunk Size = 1024**

* Best context continuity
* Suitable for complex document understanding tasks
* Higher latency and cost should be expected

---

## Final Conclusion

The experiment demonstrates that increasing chunk size does not necessarily reduce end-to-end RAG latency. While larger chunks reduce the number of vectors stored and searched, the latency savings are outweighed by the increased token processing burden on the LLM.

For this dataset and GPT-4o-based RAG pipeline:

**Chunk Size 256 achieved the best latency (1.43s), while Chunk Size 512 offers the most balanced trade-off between retrieval quality and response speed.**
