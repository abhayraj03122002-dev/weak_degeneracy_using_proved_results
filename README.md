# Efficient Weak Degeneracy Computation using Degeneracy Bounds

## 📌 Overview

This repository focuses on the **computation of weak degeneracy of graphs**, a structural parameter that is generally **difficult to compute directly**.

To address this, we implement a **multi-strategy framework** combining:

* **Theoretical graph results**
* **Algorithmic upper bounds**
* **Optimized bounded search**

This hybrid approach significantly reduces computational complexity compared to naive brute-force methods.

---

## 📖 Mathematical Background

### 🔹 Degeneracy

A graph ( G ) is said to be **d-degenerate** if every subgraph of ( G ) contains a vertex of degree at most ( d ).

Equivalently:

> Degeneracy is the smallest integer ( d ) such that vertices can be removed iteratively with degree ≤ ( d ).

---

### 🔹 Weak Degeneracy

Weak degeneracy generalizes the deletion process by allowing controlled reductions via a function ( f(v) ), subject to constraints.

It is computationally harder because:

* It involves **global feasibility conditions**
* Requires **search over possible assignments**

---

### 🔹 Key Relation

```
weak degeneracy(G) ≤ degeneracy(G)
```

This inequality is central to our approach.

---

## ⚙️ Algorithmic Framework

The repository follows a **three-step pipeline**:

### Step 1: Compute Degeneracy (Upper Bound)

* Use a greedy algorithm:

  * Repeatedly remove vertex with minimum degree
* Output gives:

  ```
  upper bound for weak degeneracy
  ```

---

### Step 2: Apply Theoretical Bounds

* Detect special graph classes:

  * Trees
  * Complete graphs
  * Complete bipartite graphs
  * Planar graphs (girth + forbidden cycles)
  * Icosahedral graph
* Directly infer weak degeneracy without search

---

### Step 3: Bounded Search Refinement

* Search within range:

  ```
  [start_d, degeneracy(G)]
  ```
* Use recursive deletion feasibility:

  * Assign ( f(v) = d )
  * Try all valid deletions
  * Stop early when failure occurs

---

## 📂 Files Description

### `weak_degeneracy_theory.py`

* Uses **graph-theoretic results**
* Avoids brute-force computation
* Efficient for structured graphs

---

### `degeneracy.py`

* Implements **greedy degeneracy algorithm**
* Time Complexity:

  ```
  O(V^2)  (current implementation)
  ```
* Can be optimized using priority queues

---

### `weak_degeneracy_search.py`

* Implements **recursive backtracking**

* Uses:

  * bounded range
  * early stopping

* Time Complexity:

  ```
  Exponential (worst case)
  ```

  but practically reduced due to pruning

---

## ▶️ Usage

### Step 1: Apply Theoretical Bounds

```bash
python weak_degeneracy_theory.py
```

### Step 2: Compute Degeneracy

```bash
python degeneracy.py
```

### Step 3: Refine Using Search

```bash
python weak_degeneracy_search.py
```

---

## 📊 Input Format

```
Enter number of vertices: n
Enter number of edges: m
Enter edges (u v):
```

### Example

```
5
4
0 1
1 2
2 3
3 4
```

---

## ✅ Example Execution

```
Degeneracy(G) = 2
Search Range = [1, 2]

Weak Degeneracy(G) = 1
```

---

## 🚀 Key Features

* Hybrid approach: **theory + algorithms + search**
* Uses **degeneracy as an effective upper bound**
* Avoids unnecessary brute-force exploration
* Incorporates **early stopping optimization**
* Works with **custom graph inputs**

---

## 🔗 How Components Work Together

```
Input Graph
     ↓
Apply Theoretical Results
     ↓
Compute Degeneracy (Upper Bound)
     ↓
Refine via Bounded Search
     ↓
Final Weak Degeneracy
```

---

## 📦 Requirements

Create a `requirements.txt`:

```
networkx
```

Install using:

```bash
pip install -r requirements.txt
```

---

## 📈 Future Work

* Try parallel programming to speed up the recursive search.
* Use memoization to avoid solving the same subproblem again.
* Improve the algorithm by reducing unnecessary branches.
* Find better theoretical bounds to reduce the search range.

---


## 🎯 Research Motivation

Weak degeneracy is an important structural parameter in graph theory, but:

* Direct computation is **computationally expensive**
* Few **practical implementations** exist

This project provides:

* A **computational framework**
* A combination of **theoretical and algorithmic techniques**
* A **practical tool for experimentation and research**

---

## 👤 Author

**Abhay Kumar**
MSc Mathematics and Computing
IIT Bhilai

---

## 📌 Note

This repository is useful for:

* Graph Theory research
* Algorithm design
* Structural graph analysis
* Academic projects and PhD preparation
