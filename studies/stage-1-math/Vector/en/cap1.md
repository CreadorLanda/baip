# Chapter 1 — Vectors, what even are they?

**English** · [Português](../pt/cap1.md)

> **“The introduction of numbers as coordinates is an act of violence.”**
> — Hermann Weyl

**Source:** [3Blue1Brown — Essence of Linear Algebra, chapter 1](https://www.youtube.com/watch?v=fNk_zzaMoSs)

---

## 1. The cornerstone of linear algebra

The cornerstone of **linear algebra** is the **vector**.

There are three distinct but related ideas of what a vector is:

1. the **physics** perspective;
2. the **computer science** perspective;
3. the **mathematics** perspective.

They are different ways of seeing the same concept, and they are deeply connected.

## 2. Three perspectives on vectors

### 2.1. Physics: an arrow

In physics, a vector is an **arrow pointing in some direction in space**. What defines it is:

- its **length** (magnitude);
- its **direction**.

As long as these two things don't change, you can move the arrow around and it is still **the same vector**.

Vectors that live in a **plane** are two-dimensional; those in the space we usually picture are **three-dimensional**.

### 2.2. Computer science: a list of numbers

In computer science, a vector is simply an **ordered list of numbers**.

```math
\begin{bmatrix} 3 \\ 2 \end{bmatrix}
\qquad
\begin{bmatrix} 3 \\ 2 \\ 5 \end{bmatrix}
```

The first has two numbers, so it is a vector in **two dimensions**; the second has three, so it is a vector in **three dimensions**.

From this point of view, the **dimension of a vector is the length of the list**. Order matters: $[3, 2]$ and $[2, 3]$ are different vectors.

> **Note:** this is the view of vectors we will use most in programming, AI and machine learning — an image, a sentence or a user all become lists of numbers.

### 2.3. Mathematics: anything you can add and scale

The mathematical view generalizes the other two. A vector is **any object** for which two operations make sense:

- **adding** two vectors;
- **multiplying** a vector by a number.

Arrows and lists of numbers are examples, but not the only ones — functions, for instance, can be vectors too.

## 3. How we will think about vectors in this chapter

We will think of a vector as an **arrow in a coordinate system**, with its **tail at the origin**.

This differs from physics, where a vector can sit anywhere. In linear algebra, almost always, the vector is **rooted at the origin**. That choice is what lets us move between the arrow and the list of numbers.

## 4. The coordinate system

We start in **two dimensions**, with two axes:

- the **$x$-axis**, horizontal;
- the **$y$-axis**, vertical.

The point where they cross is the **origin** — the center of space and the starting point of every vector.

| Axis | Positive number | Negative number |
|------|-----------------|-----------------|
| $x$  | right           | left            |
| $y$  | up              | down            |

## 5. The coordinates of a vector

A vector's coordinates are **instructions for getting from its tail to its tip**.

```math
\vec{v} = \begin{bmatrix} 3 \\ 2 \end{bmatrix}
```

- The first number tells you **how far to walk along the $x$-axis**: 3 units to the right.
- The second tells you **how far to walk along the $y$-axis**: 2 units up.

Where you end up is the tip of the vector.

![The vector [3, 2]: 3 units right, then 2 up](../img/vector-coordinates.svg)

### Vector or point?

To tell them apart, the convention is:

- **vector** → coordinates written **vertically**, in square brackets (inline we write $[3, 2]$);
- **point** → coordinates written **horizontally**, in parentheses.

```math
\underbrace{\begin{bmatrix} 3 \\ 2 \end{bmatrix}}_{\text{vector}}
\qquad
\underbrace{(3, 2)}_{\text{point}}
```

## 6. An important correspondence

> **Every pair of numbers gives exactly one vector, and every vector in the plane corresponds to exactly one pair of numbers.**

That is why we can move freely between the arrow and the list of numbers.

## 7. Vectors in three dimensions

In three dimensions we add a third axis, the **$z$-axis**, perpendicular to both $x$ and $y$. Each vector becomes an **ordered triplet of numbers**:

```math
\begin{bmatrix} x \\ y \\ z \end{bmatrix}
```

- the first number says how far to move along the $x$-axis;
- the second, how far to move parallel to the $y$-axis;
- the third, how far to move parallel to the $z$-axis.

For example, $[3, 2, 5]$ means 3 units in $x$, 2 in $y$ and 5 in $z$.

> **Every triplet of numbers gives exactly one vector in space, and every vector in space corresponds to exactly one triplet.**

## 8. Vector addition

### Geometrically: tip to tail

To add $\vec{a}$ and $\vec{b}$:

1. leave $\vec{a}$ where it is;
2. move $\vec{b}$ so that its **tail sits at the tip of $\vec{a}$**;
3. draw a vector from the **tail of $\vec{a}$** to the **tip of $\vec{b}$**.

That new vector is $\vec{a} + \vec{b}$.

![Vector addition: a = [1, 2], b = [3, −1], a + b = [4, 1]](../img/vector-addition.svg)

> **Note:** this is about the only time in linear algebra we let a vector leave the origin — just to visualize the sum. The result is drawn from the origin again.

### Numerically: coordinate by coordinate

Add each coordinate to the matching coordinate:

```math
\begin{bmatrix} a_1 \\ a_2 \end{bmatrix}
+
\begin{bmatrix} b_1 \\ b_2 \end{bmatrix}
=
\begin{bmatrix} a_1 + b_1 \\ a_2 + b_2 \end{bmatrix}
\qquad\text{e.g.}\qquad
\begin{bmatrix} 1 \\ 2 \end{bmatrix}
+
\begin{bmatrix} 3 \\ -1 \end{bmatrix}
=
\begin{bmatrix} 4 \\ 1 \end{bmatrix}
```

**Why it works:** following the instructions of $\vec{a}$ and then those of $\vec{b}$ is the same as walking a total of $1 + 3 = 4$ in $x$ and $2 + (-1) = 1$ in $y$.

## 9. Multiplication by a scalar

Multiplying a vector by a number **stretches, squishes or flips** it. That number is called a **scalar**, and the operation is **scalar multiplication** (*scaling*). With $\vec{v} = [2, 1]$:

| Scalar $c$      | Effect on $c\vec{v}$                                                       |
|-----------------|----------------------------------------------------------------------------|
| $c > 1$         | stretches: $2\vec{v}$ is twice as long                                     |
| $0 < c < 1$     | squishes: $\tfrac{1}{2}\vec{v}$ is half as long                            |
| $c = 0$         | gives the zero vector $[0, 0]$                                             |
| $c < 0$         | flips it (same line, opposite way) and scales it by $\lvert c \rvert$      |

![v = [2, 1], 2v = [4, 2] and −2v = [−4, −2]](../img/scalar-multiplication.svg)

### Numerically

Multiply **each coordinate** by the scalar:

```math
2 \begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} 4 \\ 2 \end{bmatrix}
\qquad
-2 \begin{bmatrix} 2 \\ 1 \end{bmatrix} = \begin{bmatrix} -4 \\ -2 \end{bmatrix}
```

The minus sign flips the direction; the $2$ doubles the length.

## 10. In code

In Python, a vector is a list — or, in practice, a NumPy array:

```python
import numpy as np

a = np.array([1, 2])
b = np.array([3, -1])

a + b      # array([4, 1])    coordinate-by-coordinate addition
2 * a      # array([2, 4])    scales every coordinate
-1 * a     # array([-1, -2])  same length, opposite direction

# the same without NumPy
[x + y for x, y in zip([1, 2], [3, -1])]   # [4, 1]
```

## 11. Summary

| Concept                   | Key idea                                                     |
|---------------------------|--------------------------------------------------------------|
| **Vector — physics**      | An arrow defined by length and direction                     |
| **Vector — CS**           | An ordered list of numbers                                   |
| **Vector — math**         | Anything that can be added and multiplied by scalars         |
| **2D vector**             | $[x, y]$ — two coordinates                                   |
| **3D vector**             | $[x, y, z]$ — three coordinates                              |
| **Point**                 | $(x, y)$ — different notation from a vector                  |
| **Origin**                | Where every vector's tail sits                               |
| **Addition**              | Tip to tail; numerically, coordinate by coordinate           |
| **Scalar**                | A number that multiplies a vector                            |
| **Scalar multiplication** | Stretches or squishes the vector; multiplies each coordinate |
| **Negative scalar**       | Flips the direction and scales by the absolute value         |

## 12. The big idea

> **A vector can be seen as an arrow, represented as a list of numbers, and manipulated with two operations: addition and scalar multiplication.**

Linear algebra lives in the translation between these two views: the geometric one for intuition, and the numeric one for computation.

## 13. Check your understanding

1. Compute $[1, 2] + [3, -1]$.
2. Compute $3 \cdot [-1, 2]$.
3. Compute $2 \cdot [1, 0] + 3 \cdot [0, 1]$.
4. What happens geometrically to a vector when you multiply it by $-1$?
5. What is the difference between the point $(3, 2)$ and the vector $[3, 2]$?

<details>
<summary>Answers</summary>

1. $[4, 1]$
2. $[-3, 6]$
3. $[2, 3]$ — any 2D vector can be written this way; that is the idea of a **basis**, in the next chapter.
4. It keeps the same length and points the opposite way.
5. The point is a position; the vector is the arrow from the origin to that position (or, more generally, a displacement).

</details>
