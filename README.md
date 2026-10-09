# 🧠 BAIP — Becoming an AI Professional

**English** · [Português](README.pt.md)

> Learning AI in public. Building AI, not just using it.

A 24-month, project-driven roadmap from math foundations to your own AI research.
Every stage is tracked as GitHub issues you can generate in your own repository,
in your own language.

**Duration:** 24 months · **Load:** 15–20 h/week · **Profile:** AI Researcher + ML Engineer + AI Systems Engineer

## 🚀 Use this roadmap

1. Fork or copy this repository.
2. Generate the issues (epics, tasks and final tests) in your language:

   ```bash
   gh auth login
   python3 scripts/sync_issues.py --lang en --apply   # or --lang pt
   ```

3. Work through the issues in order and close them as you go.

Details, customization and how to add a language: [`roadmap/README.md`](roadmap/README.md).

## 🎯 End goal

In 24 months be able to:

- Read AI papers
- Implement models
- Train and evaluate models
- Optimize inference
- Build complete AI systems
- Run experiments and benchmarks
- Do your own research

**Focus:** Machine Learning, Deep Learning, LLMs, Multimodal AI, AI Agents, Model Training, GPU/AI Systems, Model Optimization, Research

## ⏰ Suggested weekly schedule

| Day | Focus |
|-----|-------|
| Monday | Math |
| Tuesday | ML / Deep Learning |
| Wednesday | Math + implementation |
| Thursday | AI + papers |
| Friday | Project |
| Saturday | 🔥 Heavy project — 4–5 h |
| Sunday | Review + paper — ~2 h |

## 🗺️ Stages

**🟢 Stage 1 — Months 1–3: Math foundations**
- Month 1 · Linear algebra: vectors, matrices, linear systems, eigenvalues, SVD, PCA
- Month 2 · Calculus: derivatives, gradient, chain rule, Jacobian, gradient descent
- Month 3 · Probability: Bayes, distributions, entropy, cross-entropy, KL

**🔵 Stage 2 — Months 4–6: Machine Learning**
- Month 4 · Linear / logistic regression, loss, train/test
- Month 5 · k-NN, trees, random forest, SVM, naive Bayes, clustering
- Month 6 · Overfitting, bias/variance, regularization, cross-validation, metrics

**🔴 Stage 3 — Months 7–9: Deep Learning**
- Month 7 · PyTorch, perceptron, MLP
- Month 8 · CNN — image classifier
- Month 9 · RNN / LSTM / GRU — text classifier / generator

**🟣 Stage 4 — Months 10–12: Transformers**
- Month 10 · Attention `softmax(QKᵀ/√dₖ)V`
- Month 11 · Multi-head attention, positional encoding, LayerNorm, residuals
- Month 12 · **Tiny LLM** — your own Transformer

**🟠 Stage 5 — Months 13–15: LLM Engineering**
- Tokenizers, BPE, Hugging Face, SFT, LoRA / QLoRA, quantization, **RAG system**

**🟡 Stage 6 — Months 16–17: AI Agents**
- Tool calling, planning, memory, loops, multi-agent → **AI agent**

**🟢 Stage 7 — Months 18–19: Multimodal AI**
- Vision (ViT, CLIP), audio, video → **Conductor model** (image / video / text orchestrator)

**⚙️ Stage 8 — Months 20–21: AI Systems**
- GPU / CUDA, quantization, pruning, batching, KV cache, distributed systems

**🔬 Stage 9 — Months 22–24: Research Mode**
- 2–4 papers/week, reproduce results, own research

## 🏆 The 12 projects

| # | Project | Folder |
|---|---------|--------|
| 01 | Math from scratch | `projects/01-math-from-scratch/` |
| 02 | Classic ML library from scratch | `projects/02-classic-ml/` |
| 03 | Autograd engine | `projects/03-autograd-engine/` |
| 04 | Neural network framework | `projects/04-nn-framework/` |
| 05 | Tiny LLM | `projects/05-tiny-llm/` |
| 06 | RAG system | `projects/06-rag-system/` |
| 07 | AI agent | `projects/07-ai-agent/` |
| 08 | Multimodal AI | `projects/08-multimodal/` |
| 09 | Conductor model | `projects/09-conductor/` |
| 10 | AI runtime | `projects/10-ai-runtime/` |
| 11 | AI integration — bring AI into a tool or language you own | `projects/11-ai-integration/` |
| 12 | Own research | `projects/12-research/` |

Give them your own names — the folders are just a starting point.

## 🧠 Learning rule

```
LEARN → IMPLEMENT → USE → BREAK → REBUILD → EXPLAIN
```

> If you can't explain why it works mathematically and implement a simplified version, you're not done.

## 📁 Folders

```
studies/stage-1-math/ … stage-9-research/   study notes per stage
projects/01-math-from-scratch/ … 12-research/  project code
notes/        free notes
papers/       paper summaries
blog/posts/   blog posts
roadmap/      roadmap data + translations (source of the GitHub issues)
scripts/      tooling (issue sync)
```

## 🧬 Stack

Python, PyTorch, NumPy, Julia, C/C++/Rust/Zig, CUDA, Linux + Git + Docker, Hugging Face

---

Created by [Alexandre Landa](https://github.com/CreadorLanda) · [MIT License](LICENSE)
