# Capítulo 1 — Vetores: o que são, afinal?

[English](../en/cap1.md) · **Português**

> **“A introdução de números como coordenadas é um ato de violência.”**
> — Hermann Weyl

**Fonte:** [3Blue1Brown — Essence of Linear Algebra, capítulo 1](https://www.youtube.com/watch?v=fNk_zzaMoSs)

---

## 1. A pedra fundamental da Álgebra Linear

A pedra fundamental da **Álgebra Linear** é o **vetor**.

Existem três ideias distintas, mas relacionadas, sobre o que é um vetor:

1. a perspectiva da **Física**;
2. a perspectiva da **Ciência da Computação**;
3. a perspectiva da **Matemática**.

São formas diferentes de ver o mesmo conceito, e estão profundamente ligadas.

## 2. As três perspectivas sobre vetores

### 2.1. Física: uma seta

Na Física, um vetor é uma **seta que aponta numa direção do espaço**. O que o define é:

- o seu **tamanho** (magnitude);
- a sua **direção** (e sentido).

Enquanto estas duas coisas não mudarem, podemos mover a seta pelo espaço e continua a ser **o mesmo vetor**.

Os vetores que vivem num **plano** são bidimensionais; os que vivem no espaço que normalmente imaginamos são **tridimensionais**.

### 2.2. Ciência da Computação: uma lista de números

Na Ciência da Computação, um vetor é simplesmente uma **lista ordenada de números**.

```math
\begin{bmatrix} 3 \\ 2 \end{bmatrix}
\qquad
\begin{bmatrix} 3 \\ 2 \\ 5 \end{bmatrix}
```

O primeiro tem dois números, por isso é um vetor em **duas dimensões**; o segundo tem três, por isso é um vetor em **três dimensões**.

Nesta perspectiva, a **dimensão do vetor é o tamanho da lista**. A ordem importa: $[3, 2]$ e $[2, 3]$ são vetores diferentes.

> **Nota:** esta é a forma de ver vetores que mais vamos usar em programação, IA e Machine Learning — uma imagem, uma frase ou um utilizador viram listas de números.

### 2.3. Matemática: qualquer coisa que se possa somar e escalar

A perspectiva matemática generaliza as outras duas. Um vetor é **qualquer objeto** para o qual façam sentido duas operações:

- **somar** dois vetores;
- **multiplicar** um vetor por um número.

Setas e listas de números são exemplos, mas não os únicos — funções, por exemplo, também podem ser vetores.

## 3. Como vamos pensar nos vetores neste capítulo

Vamos pensar num vetor como uma **seta num sistema de coordenadas**, com a **cauda na origem**.

Isto é diferente da Física: lá o vetor pode estar em qualquer sítio. Em Álgebra Linear, em praticamente todos os casos, o vetor fica **preso à origem**. Esta escolha é o que permite passar da seta para a lista de números e vice-versa.

## 4. Sistema de coordenadas

Começamos em **duas dimensões**, com dois eixos:

- o **eixo $x$**, horizontal;
- o **eixo $y$**, vertical.

O ponto onde se cruzam é a **origem** — o centro do espaço e o ponto de partida de todos os vetores.

| Eixo | Número positivo | Número negativo |
|------|-----------------|-----------------|
| $x$  | para a direita  | para a esquerda |
| $y$  | para cima       | para baixo      |

## 5. Coordenadas de um vetor

As coordenadas de um vetor são **instruções para ir da cauda até à ponta**.

```math
\vec{v} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}
```

- O primeiro número diz **quanto andar no eixo $x$**: 3 unidades para a direita.
- O segundo diz **quanto andar no eixo $y$**: 2 unidades para cima.

Onde chegamos é a ponta do vetor.

![O vetor [3, 2]: 3 unidades para a direita e depois 2 para cima](../img/vector-coordinates.svg)

### Vetor ou ponto?

Para distinguir os dois, a convenção é:

- **vetor** → coordenadas na **vertical**, entre parêntesis retos (em texto corrido escrevemos $[3, 2]$);
- **ponto** → coordenadas na **horizontal**, entre parêntesis curvos.

```math
\underbrace{\begin{bmatrix} 3 \\ 2 \end{bmatrix}}_{\text{vetor}}
\qquad
\underbrace{(3, 2)}_{\text{ponto}}
```

## 6. Uma correspondência importante

> **Cada par de números determina exatamente um vetor, e cada vetor no plano corresponde exatamente a um par de números.**

Por isso podemos passar livremente da seta para a lista de números e de volta.

## 7. Vetores em três dimensões

Em três dimensões juntamos um terceiro eixo, o **eixo $z$**, perpendicular a $x$ e a $y$. Cada vetor passa a ser uma **trinca ordenada de números**:

```math
\begin{bmatrix} x \\ y \\ z \end{bmatrix}
```

- o primeiro número diz quanto andar ao longo do eixo $x$;
- o segundo, quanto andar paralelamente ao eixo $y$;
- o terceiro, quanto andar paralelamente ao eixo $z$.

Por exemplo, $[3, 2, 5]$ significa 3 unidades em $x$, 2 em $y$ e 5 em $z$.

> **Cada trinca de números determina exatamente um vetor no espaço, e cada vetor no espaço corresponde exatamente a uma trinca.**

## 8. Soma de vetores

### Geometricamente: ponta com cauda

Para somar $\vec{a}$ e $\vec{b}$:

1. deixamos $\vec{a}$ onde está;
2. movemos $\vec{b}$ para que a sua **cauda fique na ponta de $\vec{a}$**;
3. desenhamos um vetor da **cauda de $\vec{a}$** até à **ponta de $\vec{b}$**.

Esse novo vetor é $\vec{a} + \vec{b}$.

![Soma de vetores: a = [1, 2], b = [3, −1], a + b = [4, 1]](../img/vector-addition.svg)

> **Nota:** esta é praticamente a única vez em Álgebra Linear em que deixamos um vetor sair da origem — só para visualizar a soma. O resultado volta a ser desenhado a partir da origem.

### Numericamente: coordenada a coordenada

Somamos cada coordenada com a coordenada correspondente:

```math
\begin{bmatrix} a_1 \\ a_2 \end{bmatrix}
+
\begin{bmatrix} b_1 \\ b_2 \end{bmatrix}
=
\begin{bmatrix} a_1 + b_1 \\ a_2 + b_2 \end{bmatrix}
\qquad\text{ex.:}\qquad
\begin{bmatrix} 1 \\ 2 \end{bmatrix}
+
\begin{bmatrix} 3 \\ -1 \end{bmatrix}
=
\begin{bmatrix} 4 \\ 1 \end{bmatrix}
```

**Porque é que funciona:** seguir as instruções de $\vec{a}$ e depois as de $\vec{b}$ é o mesmo que andar, no total, $1 + 3 = 4$ em $x$ e $2 + (-1) = 1$ em $y$.

## 9. Multiplicação por um escalar

Multiplicar um vetor por um número **estica, encolhe ou inverte** o vetor. Esse número chama-se **escalar** e a operação chama-se **multiplicação escalar** (*scaling*). Com $\vec{v} = [2, 1]$:

| Escalar $c$     | Efeito em $c\vec{v}$                                                   |
|-----------------|------------------------------------------------------------------------|
| $c > 1$         | estica: $2\vec{v}$ tem o dobro do tamanho                              |
| $0 < c < 1$     | encolhe: $\tfrac{1}{2}\vec{v}$ tem metade do tamanho                   |
| $c = 0$         | dá o vetor nulo $[0, 0]$                                               |
| $c < 0$         | inverte o sentido (mesma reta, aponta para o lado oposto) e escala por $\lvert c \rvert$ |

![v = [2, 1], 2v = [4, 2] e −2v = [−4, −2]](../img/scalar-multiplication.svg)

### Numericamente

Multiplicamos **cada coordenada** pelo escalar:

```math
2 \begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 4 \\ 2 \end{bmatrix}
\qquad
-2 \begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} -4 \\ -2 \end{bmatrix}
```

O sinal negativo inverte o sentido; o $2$ dobra o tamanho.

## 10. Em código

Em Python, um vetor é uma lista — ou, na prática, um array NumPy:

```python
import numpy as np

a = np.array([1, 2])
b = np.array([3, -1])

a + b      # array([4, 1])    soma coordenada a coordenada
2 * a      # array([2, 4])    escala cada coordenada
-1 * a     # array([-1, -2])  mesmo tamanho, sentido oposto

# o mesmo sem NumPy
[x + y for x, y in zip([1, 2], [3, -1])]   # [4, 1]
```

## 11. Resumo

| Conceito               | Ideia principal                                                 |
|------------------------|-----------------------------------------------------------------|
| **Vetor — Física**     | Uma seta definida por tamanho e direção                         |
| **Vetor — Computação** | Uma lista ordenada de números                                   |
| **Vetor — Matemática** | Um objeto que pode ser somado e multiplicado por escalares      |
| **Vetor em 2D**        | $[x, y]$ — duas coordenadas                                     |
| **Vetor em 3D**        | $[x, y, z]$ — três coordenadas                                  |
| **Ponto**              | $(x, y)$ — notação diferente da de um vetor                     |
| **Origem**             | Onde fica a cauda de todos os vetores                           |
| **Soma**               | Ponta com cauda; numericamente, coordenada a coordenada         |
| **Escalar**            | Número que multiplica um vetor                                  |
| **Multiplicação escalar** | Estica ou encolhe o vetor; multiplica cada coordenada        |
| **Escalar negativo**   | Inverte o sentido e escala pelo valor absoluto                  |

## 12. Ideia central

> **Um vetor pode ser visto como uma seta, representado como uma lista de números e manipulado com duas operações: soma e multiplicação por escalares.**

A Álgebra Linear vive da passagem entre estas duas visões: a geométrica, para ter intuição, e a numérica, para calcular.

## 13. Verifica se percebeste

1. Calcula $[1, 2] + [3, -1]$.
2. Calcula $3 \cdot [-1, 2]$.
3. Calcula $2 \cdot [1, 0] + 3 \cdot [0, 1]$.
4. O que acontece geometricamente a um vetor quando o multiplicas por $-1$?
5. Qual é a diferença entre o ponto $(3, 2)$ e o vetor $[3, 2]$?

<details>
<summary>Respostas</summary>

1. $[4, 1]$
2. $[-3, 6]$
3. $[2, 3]$ — qualquer vetor 2D pode ser escrito assim; é a ideia de **base**, no próximo capítulo.
4. Fica com o mesmo tamanho e aponta no sentido oposto.
5. O ponto é uma posição; o vetor é a seta da origem até essa posição (ou, de forma geral, um deslocamento).

</details>
