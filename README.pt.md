# 🧠 BAIP — Becoming an AI Professional

[English](README.md) · **Português**

> Aprender IA em público. Construir IA, não só usar.

Um roadmap de 24 meses, guiado por projetos, dos fundamentos de matemática até
pesquisa própria em IA. Cada etapa é acompanhada por issues do GitHub que podes
gerar no teu próprio repositório, na tua língua.

**Duração:** 24 meses · **Carga:** 15–20 h/semana · **Perfil:** AI Researcher + ML Engineer + AI Systems Engineer

## 🚀 Usar este roadmap

1. Faz fork ou copia este repositório.
2. Gera as issues (epics, tasks e testes finais) na tua língua:

   ```bash
   gh auth login
   python3 scripts/sync_issues.py --lang pt --apply   # ou --lang en
   ```

3. Segue as issues por ordem e fecha-as à medida que avanças.

Detalhes, personalização e como adicionar uma língua: [`roadmap/README.md`](roadmap/README.md).

## 🎯 Objetivo final

Em 24 meses conseguir:

- Compreender papers de IA
- Implementar modelos
- Treinar e avaliar modelos
- Otimizar inferência
- Criar sistemas de IA completos
- Fazer experiências e benchmarks
- Desenvolver pesquisa própria

**Foco:** Machine Learning, Deep Learning, LLMs, Multimodal AI, AI Agents, Model Training, GPU/AI Systems, Model Optimization, Research

## ⏰ Carga semanal sugerida

| Dia | Foco |
|-----|------|
| Segunda | Matemática |
| Terça | ML / Deep Learning |
| Quarta | Matemática + implementação |
| Quinta | IA + papers |
| Sexta | Projeto |
| Sábado | 🔥 Projeto pesado — 4–5 h |
| Domingo | Revisão + paper — ~2 h |

## 🗺️ Etapas

**🟢 Etapa 1 — Meses 1–3: Fundamentos matemáticos**
- Mês 1 · Álgebra linear: vetores, matrizes, sistemas lineares, autovalores, SVD, PCA
- Mês 2 · Cálculo: derivadas, gradiente, regra da cadeia, Jacobiano, gradient descent
- Mês 3 · Probabilidade: Bayes, distribuições, entropia, cross-entropy, KL

**🔵 Etapa 2 — Meses 4–6: Machine Learning**
- Mês 4 · Regressão linear / logística, loss, treino/teste
- Mês 5 · k-NN, árvores, random forest, SVM, naive Bayes, clustering
- Mês 6 · Overfitting, bias/variance, regularização, cross-validation, métricas

**🔴 Etapa 3 — Meses 7–9: Deep Learning**
- Mês 7 · PyTorch, perceptron, MLP
- Mês 8 · CNN — classificador de imagens
- Mês 9 · RNN / LSTM / GRU — classificador / gerador de texto

**🟣 Etapa 4 — Meses 10–12: Transformers**
- Mês 10 · Attention `softmax(QKᵀ/√dₖ)V`
- Mês 11 · Multi-head attention, positional encoding, LayerNorm, residuais
- Mês 12 · **Tiny LLM** — o teu próprio Transformer

**🟠 Etapa 5 — Meses 13–15: LLM Engineering**
- Tokenizers, BPE, Hugging Face, SFT, LoRA / QLoRA, quantização, **sistema RAG**

**🟡 Etapa 6 — Meses 16–17: AI Agents**
- Tool calling, planeamento, memória, loops, multi-agente → **agente de IA**

**🟢 Etapa 7 — Meses 18–19: Multimodal AI**
- Visão (ViT, CLIP), áudio, vídeo → **Conductor model** (orquestrador de imagem / vídeo / texto)

**⚙️ Etapa 8 — Meses 20–21: AI Systems**
- GPU / CUDA, quantização, pruning, batching, KV cache, sistemas distribuídos

**🔬 Etapa 9 — Meses 22–24: Research Mode**
- 2–4 papers/semana, reproduzir resultados, pesquisa própria

## 🏆 Os 12 projetos

| # | Projeto | Pasta |
|---|---------|-------|
| 01 | Matemática do zero | `projects/01-math-from-scratch/` |
| 02 | Biblioteca de ML clássico do zero | `projects/02-classic-ml/` |
| 03 | Motor de autograd | `projects/03-autograd-engine/` |
| 04 | Framework de redes neuronais | `projects/04-nn-framework/` |
| 05 | Tiny LLM | `projects/05-tiny-llm/` |
| 06 | Sistema RAG | `projects/06-rag-system/` |
| 07 | Agente de IA | `projects/07-ai-agent/` |
| 08 | IA multimodal | `projects/08-multimodal/` |
| 09 | Conductor model | `projects/09-conductor/` |
| 10 | Runtime de IA | `projects/10-ai-runtime/` |
| 11 | Integração de IA — levar IA a uma ferramenta ou linguagem tua | `projects/11-ai-integration/` |
| 12 | Pesquisa própria | `projects/12-research/` |

Dá-lhes os teus próprios nomes — as pastas são só um ponto de partida.

## 🧠 Regra de aprendizagem

```
APRENDE → IMPLEMENTA → USA → QUEBRA → RECONSTRÓI → EXPLICA
```

> Se não consegues explicar por que funciona matematicamente e implementar uma versão simplificada, ainda não terminaste.

## 📁 Pastas

```
studies/stage-1-math/ … stage-9-research/   notas de estudo por etapa
projects/01-math-from-scratch/ … 12-research/  código dos projetos
notes/        notas livres
papers/       resumos de papers
blog/posts/   posts do blog
roadmap/      dados do roadmap + traduções (origem das issues do GitHub)
scripts/      ferramentas (sincronização de issues)
```

As pastas têm nomes em inglês para serem iguais em todas as línguas.

## 🧬 Tecnologias

Python, PyTorch, NumPy, Julia, C/C++/Rust/Zig, CUDA, Linux + Git + Docker, Hugging Face

---

Criado por [Alexandre Landa](https://github.com/CreadorLanda) · [Licença MIT](LICENSE)
