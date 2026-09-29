# Capítulo 1 — A Essência da Álgebra Linear

> **“A introdução de números como coordenadas é um ato de violência.”**
> — Hermann Weyl

---

## 1. A pedra fundamental da Álgebra Linear

A pedra fundamental da **Álgebra Linear** é o **vetor**.

Existem três ideias distintas, mas relacionadas, sobre o que é um vetor. Podemos entendê-lo através de três perspectivas:

1. **Perspectiva da Física**
2. **Perspectiva da Matemática**
3. **Perspectiva da Ciência da Computação**

Apesar de serem formas diferentes de enxergar o mesmo conceito, essas perspectivas estão profundamente relacionadas.

---

# 2. As três perspectivas sobre vetores

## 2.1. Perspectiva da Física

Na Física, podemos pensar nos vetores como **setas que apontam para alguma direção no espaço**.

O que define um vetor é principalmente:

* seu **tamanho** (magnitude);
* a **direção** para a qual ele aponta.

Enquanto essas características não mudarem, podemos mover o vetor pelo espaço e ele continuará representando o **mesmo vetor**.

> **Representação sugerida:** desenhar uma mesma seta em diferentes posições, mantendo o mesmo tamanho e direção.

Os vetores que vivem em **planos** são bidimensionais, enquanto os vetores que vivem no espaço que normalmente imaginamos são **tridimensionais**.

---

## 2.2. Perspectiva da Ciência da Computação

Na Ciência da Computação, um vetor pode ser visto simplesmente como uma **lista ordenada de números**.

Por exemplo:

$$
\begin{bmatrix}
3\\
2
\end{bmatrix}
$$

Esse vetor possui dois números e, por isso, representa um vetor em **duas dimensões**.

Já:

$$
\begin{bmatrix}
3\\
2\\
5
\end{bmatrix}
$$

possui três números e representa um vetor em **três dimensões**.

Assim, nessa perspectiva, a **dimensão do vetor é determinada pelo tamanho da lista de números**.

> **Nota:** essa forma de enxergar vetores será especialmente importante quando começarmos a trabalhar com programação, computação gráfica, IA e Machine Learning.

---

## 2.3. Perspectiva da Matemática

A perspectiva matemática combina, de certa forma, as ideias apresentadas pela Física e pela Ciência da Computação.

De maneira geral, podemos pensar em um vetor como qualquer objeto que possua uma noção de:

* **soma de vetores**;
* **multiplicação de um vetor por um número**.

Isso é importante porque, em Matemática, o conceito de vetor pode ser muito mais amplo do que simplesmente uma seta desenhada em um plano.

---

# 3. Como vamos pensar nos vetores neste capítulo

Apesar de existirem diferentes maneiras de interpretar um vetor, neste capítulo vamos adotar uma representação específica.

Vamos pensar no vetor como uma **seta em um sistema de coordenadas**, como o plano $(x,y)$, com sua **cauda situada na origem**.

Isso é um pouco diferente da perspectiva da Física.

Na Física, um vetor pode ser movido livremente pelo espaço. Já na Álgebra Linear, em praticamente todos os casos que veremos, vamos manter o vetor **preso à origem**.

Essa escolha torna muito mais fácil representar e manipular os vetores matematicamente.

---

# 4. Sistema de coordenadas

Vamos começar trabalhando em **duas dimensões**.

Temos duas linhas principais:

* uma linha vertical chamada **eixo $y$**;
* uma linha horizontal chamada **eixo $x$**.

O ponto onde esses dois eixos se cruzam é chamado de **origem**.

Podemos pensar na origem como o **centro do espaço** e o **ponto de partida de todos os vetores**.

### Direções nos eixos

No eixo $x$:

* números **positivos** → movimento para a **direita**;
* números **negativos** → movimento para a **esquerda**.

No eixo $y$:

* números **positivos** → movimento para **cima**;
* números **negativos** → movimento para **baixo**.

---

# 5. Coordenadas de um vetor

As coordenadas de um vetor são como **instruções que mostram como sair da cauda do vetor e chegar até sua ponta**.

Considere:

$$
\vec{v} =
\begin{bmatrix}
3\\
2
\end{bmatrix}
$$

O primeiro número diz **quanto devemos andar no eixo $x$**.

O segundo número diz **quanto devemos andar no eixo $y$**.

Portanto:

$$
\begin{bmatrix}
3\\
2
\end{bmatrix}
$$

significa:

1. andar **3 unidades para a direita**;
2. depois andar **2 unidades para cima**.

O resultado é a ponta do vetor.

### Uma convenção importante

Para distinguir visualmente **vetores** de **pontos**, é comum escrever as coordenadas do vetor verticalmente e colocá-las entre colchetes:

$$
\vec{v} =
\begin{bmatrix}
3\\
2
\end{bmatrix}
$$

Enquanto um ponto pode ser representado como:

$$
(3,2)
$$

Essa diferença de notação ajuda a lembrar que estamos falando de conceitos diferentes.

---

# 6. Uma relação importante

Existe uma correspondência direta entre coordenadas e vetores:

> **Cada par numérico determina um único vetor, e cada vetor está associado a um único par numérico.**

Por exemplo:

$$
\begin{bmatrix}
3\\
2
\end{bmatrix}
$$

determina exatamente um vetor.

Da mesma forma, dado um vetor em duas dimensões, podemos determinar exatamente o par de números que representa suas coordenadas.

---

# 7. Vetores em três dimensões

Agora podemos expandir nossa ideia para **três dimensões**.

Além dos eixos $x$ e $y$, adicionamos um novo eixo chamado **eixo $z$**.

O eixo $z$ é perpendicular aos eixos $x$ e $y$.

Nesse caso, cada vetor está associado a uma **trinca ordenada de números**:

$$
\begin{bmatrix}
x\\
y\\
z
\end{bmatrix}
$$

Cada número possui uma função:

* o primeiro diz quanto devemos nos mover no eixo $x$;
* o segundo diz quanto devemos nos mover paralelamente ao eixo $y$;
* o terceiro diz quanto devemos nos mover paralelamente ao eixo $z$.

Por exemplo:

$$
\begin{bmatrix}
3\\
2\\
5
\end{bmatrix}
$$

significa:

* 3 unidades no eixo $x$;
* 2 unidades no eixo $y$;
* 5 unidades no eixo $z$.

Assim:

> **Cada trinca numérica determina um único vetor no espaço, e cada vetor no espaço corresponde exatamente a uma trinca numérica.**

---

# 8. Soma de vetores

Agora chegamos a uma das operações fundamentais da Álgebra Linear: **a soma de vetores**.

Imagine que temos dois vetores:

* o primeiro aponta para cima e um pouco para a direita;
* o segundo aponta para a direita e um pouco para baixo.

Para somá-los, fazemos o seguinte:

1. Mantemos o primeiro vetor onde está.
2. Movemos o segundo vetor de maneira que sua **cauda fique na ponta do primeiro vetor**.
3. Desenhamos um novo vetor partindo da **cauda do primeiro vetor** até a **ponta do segundo vetor**.
4. Esse novo vetor representa a **soma dos dois vetores**.

Podemos representar isso como:

$$
\vec{a} + \vec{b} = \vec{c}
$$

onde $\vec{c}$ é o vetor resultante.

### Nota importante

> **Essa é praticamente a única vez na Álgebra Linear em que deixamos os vetores saírem da origem.**

Fazemos isso apenas para visualizar geometricamente a soma.

Depois, podemos representar novamente o vetor resultante com sua cauda na origem.

---

# 9. Multiplicação de vetores por números

Outra operação fundamental é multiplicar um vetor por um número.

Imagine que temos o vetor:

$$
\vec{v} =
\begin{bmatrix}
2\\
1
\end{bmatrix}
$$

Se multiplicarmos esse vetor pelo número $2$:

$$
2\vec{v}
$$

é como se **esticássemos o vetor**, fazendo com que ele tenha o dobro do tamanho original.

### Multiplicação por números positivos

Se multiplicarmos por um número maior que $1$, o vetor fica maior.

Se multiplicarmos por um número entre $0$ e $1$, ele fica menor.

### Multiplicação por números negativos

Se multiplicarmos por um número **negativo**, acontece algo interessante:

1. o vetor **inverte sua direção**;
2. depois é escalado de acordo com o valor absoluto desse número.

Por exemplo:

$$
-2\vec{v}
$$

produz um vetor com **o dobro do tamanho**, mas apontando na **direção oposta**.

---

# 10. Escalar — Dimensionamento

A multiplicação de um vetor por um número é chamada de **multiplicação escalar**, e o número utilizado é chamado de **escalar**.

Podemos pensar nisso como um processo de **dimensionamento** (*scaling*).

Numericamente, esticar ou diminuir um vetor significa simplesmente multiplicar **cada uma das suas coordenadas** pelo fator utilizado.

Por exemplo:

$$
\vec{v} =
\begin{bmatrix}
3\\
2
\end{bmatrix}
$$

Multiplicando por $2$:

$$
2\vec{v}
=
2
\begin{bmatrix}
3\\
2
\end{bmatrix}
=
\begin{bmatrix}
6\\
4
\end{bmatrix}
$$

Ou seja, multiplicamos **cada número do vetor pelo escalar**.

Da mesma forma:

$$
-2
\begin{bmatrix}
3\\
2
\end{bmatrix}
=
\begin{bmatrix}
-6\\
-4
\end{bmatrix}
$$

O sinal negativo inverte a direção, enquanto o $2$ dobra o tamanho.

---

# 11. Resumo

As ideias fundamentais deste capítulo podem ser resumidas assim:

| Conceito               | Ideia principal                                            |
| ---------------------- | ---------------------------------------------------------- |
| **Vetor — Física**     | Uma seta definida por tamanho e direção                    |
| **Vetor — Computação** | Uma lista ordenada de números                              |
| **Vetor — Matemática** | Um objeto que pode ser somado e multiplicado por escalares |
| **2D**                 | Vetores representados por $(x,y)$                          |
| **3D**                 | Vetores representados por $(x,y,z)$                        |
| **Origem**             | Ponto de partida usado para representar os vetores         |
| **Soma**               | Combinação de dois ou mais vetores                         |
| **Escalar**            | Número usado para multiplicar um vetor                     |
| **Dimensionamento**    | Aumentar ou diminuir o tamanho de um vetor                 |
| **Escalar negativo**   | Inverte a direção e altera o tamanho                       |

---

# 12. Ideia central

No fundo, este capítulo estabelece uma ideia simples:

> **Um vetor pode ser visualizado como uma seta, representado como uma lista de números e manipulado matematicamente através de operações como soma e multiplicação por escalares.**

A partir dessas ideias, podemos começar a construir praticamente toda a estrutura da **Álgebra Linear**.

---

## Fonte

Este conteúdo foi organizado a partir da explicação apresentada no vídeo:

**3Blue1Brown — Essence of Linear Algebra**

https://www.youtube.com/watch?v=fNk_zzaMoSs
