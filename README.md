# Bat Algorithm – Python Implementation

This repository contains an implementation of the **Bat Algorithm**, a nature-inspired metaheuristic proposed by Xin-She Yang, based on the echolocation behavior of bats.

The algorithm is applied to solve **global optimization problems**, and this implementation uses the **Rastrigin function** as a benchmark due to its multimodal characteristics.

---

## 📌 Algorithm Overview

- Population-based metaheuristic
- Inspired by bat echolocation
- Balances **exploration** and **exploitation**
- Uses parameters such as:
  - Frequency
  - Loudness
  - Pulse rate

---

## 🧪 Test Function

The algorithm was tested using the **Rastrigin function**, defined as:

\[
f(x) = 10n + \sum_{i=1}^{n} \left[x_i^2 - 10\cos(2\pi x_i)\right]
\]

The global minimum is located at:

\[
x = (0, 0, ..., 0), \quad f(x) = 0
\]

---

## ⚙️ Parameters Used

- Population size: 40 bats
- Maximum iterations: 150
- Frequency range: [0.0, 2.0]
- Loudness (initial): 1.0
- Pulse rate (initial): 0.1

---

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/SEU_USUARIO/bat-algorithm.git
