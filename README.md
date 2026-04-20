# Efficient Weak Degeneracy Computation using Degeneracy Bounds

## 📌 Overview

This repository focuses on the **computation of weak degeneracy of graphs**, which is generally hard to compute directly.

To address this, we implement a **multi-strategy framework**:

* Use **theoretical results** for direct computation (when applicable)
* Use **degeneracy as an upper bound**
* Perform **optimized search within a bounded range**

The repository contains three Python programs that together provide a practical and efficient approach.

---

## 📂 Files Description

### 1. `weak_degeneracy_theory.py`

* Computes **weak degeneracy using proven theoretical results**
* Handles special graph classes such as:

  * Trees
  * Complete graphs
  * Complete bipartite graphs
  * Planar graphs (using girth and forbidden cycle conditions)
  * Icosahedral graph
* Uses graph properties to **directly return bounds without brute force**

---

### 2. `degeneracy.py`

* Computes **degeneracy of a graph using its definition**
* Algorithm:

  * Repeatedly remove the vertex with **minimum degree**
  * Track the **maximum of these minimum degrees**
* This value serves as an **upper bound**:

  ```
  weak degeneracy ≤ degeneracy
  ```

---

### 3. `weak_degeneracy_search.py`

* Computes weak degeneracy using a **bounded search approach**

* Workflow:

  1. Take input range `[start_d, end_d]`
  2. Assign `f(v) = d` for all vertices
  3. Check whether graph can be fully reduced using recursive deletion
  4. Stop early when failure occurs (optimization)

* This reduces computation time significantly compared to naive brute force.

---

## ⚙️ Installation

Make sure you have Python installed. Then install dependency:

```bash
pip install networkx
```

---

## ▶️ Usage

Run each file independently:

### Step 1: Compute Degeneracy

```bash
python degeneracy.py
```

### Step 2: Use Theoretical Bounds

```bash
python weak_degeneracy_theory.py
```

### Step 3: Refine Using Search

```bash
python weak_degeneracy_search.py
```

---

## 🧠 Core Idea

Since computing weak degeneracy directly is expensive:

1. First compute:

   ```
   degeneracy(G)
   ```
2. Then use:

   ```
   weak degeneracy(G) ≤ degeneracy(G)
   ```
3. Finally search in a **restricted range** to find tighter bounds.

---

## 🚀 Key Features

* Combines **theory + algorithm + optimization**
* Avoids unnecessary brute-force computation
* Uses **early stopping strategy** for efficiency
* Supports **custom graph input**
* Built using `networkx` for graph operations

---

## 📊 Input Format

For all programs:

```
Enter number of vertices: n
Enter number of edges: m
Enter edges (u v):
```

Example:

```
5
4
0 1
1 2
2 3
3 4
```

---

## 📈 Future Improvements

* Optimize recursive search using **memoization / pruning**
* Add **file-based graph input (e.g., .txt, .csv)**
* Extend support for **larger graphs**
* Provide **visualization of graphs and deletion process**

---

## 👤 Author

Abhay Kumar
MSc Mathematics and Computing
IIT Bhilai

---

## 📌 Note

This project is useful for:

* Graph Theory research
* Algorithm design and optimization
* Understanding structural graph parameters like degeneracy and weak degeneracy
