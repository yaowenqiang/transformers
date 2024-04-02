History of AI

Word vectors

RNNs

Encoder-decoder

Attention



# Preprocessing for NLP

+ Stopwords
+ Tokenization
+ Special tokens
+ Unicode Normalization

# Attention

+ Alignment
+ Dot-product
+ Self-attention
+ Bidirectional
+ Multi-head

# Language Classification

+ Sentiment Analysis
+ Flair
+ HF Transformers
+ BERT

# Named Entity Recognition

+ SpaCy
+ Extracting Entities
+ Reddit API
+ NER with RoBERTa


# Metrics For Language

+ Extract Match(EM)
+ ROUGE
+ Recall, Precision and F1
+ Longest Common Subsequence(LCS
+ Q&A Performance with ROUGE


# Full QA Stack with Haystack

+ Haystack
+ Elasticsearch
+ TF-IDF, BM25(sparse retrivers)
+ Facebook AI Similarity Search(FAISS)
+ Dense Passage Retreiver(DPR)

# Similarity

+ Similarity in NLP
+ BERT Representations
+ Sentence Vectors
+ Similarity Metrics
+ sentence-transformers


# Fine-tuning

+ BERT Pretraining
+ Masked-Language Modeling
+ Next Sentence Prediction
+ BERT Fine-tuning
+

# NLP

+ Symbolic
+ statistical
+ Neural

> word2vec


+ Recurrent Neural Network (递归神经网络)
+ vanish gradient(梯度消失和梯度爆炸)
+ Long Short-Term Memory(长短期记忆网络LSTM)
+ Encoder-Decoder Attention()
+ Self Attention(自注意力机制)
+ Attention is all you need(paper)
+ Multi-head Attention(多头注意力)
+ Positional Encoding(位置编码)

## Special Model Tokens

| Token | Meaning |
| --- | --- |
| **[PAD]** | Padding token, allows us to maintain same-length sequences (512 tokens for Bert) even when different sized sentences are fed in |
| **[UNK]** | Used when a word is unknown to Bert |
| **[CLS]** | Appears at the start of every sequence |
| **[SEP]** | Indicates a seperator or end of sequence |
| **[MASK]** | Used when masking tokens, for example in training with masked language modelling (MLM) |+

## Stemming(词干提取)
## Lemmatization(词型还原)
