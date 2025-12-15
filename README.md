# Algoritmo do Morcego (Bat Algorithm) – Implementação em Python

Este repositório contém uma implementação do **Algoritmo do Morcego (Bat Algorithm)**, uma meta-heurística inspirada no comportamento de **ecolocalização dos morcegos**, proposta por **Xin-She Yang**.

O algoritmo pertence à área de **Inteligência de Enxame** e é utilizado para resolver **problemas de otimização global**, especialmente aqueles com muitos mínimos locais.

Este projeto foi desenvolvido com fins **acadêmicos**, como parte de um seminário da disciplina de **Inteligência Artificial**.

---

## 📌 Descrição do Algoritmo

O Algoritmo do Morcego simula o comportamento de um grupo de morcegos em busca de alimento no escuro, onde:

- Cada morcego representa uma **solução candidata**
- A posição do morcego representa uma solução no espaço de busca
- O melhor morcego encontrado representa a **melhor solução global**
- O algoritmo equilibra **exploração** e **refinamento** por meio dos parâmetros:
  - Frequência
  - Loudness (volume)
  - Taxa de pulso

Trata-se de uma **meta-heurística estocástica**, ou seja, não garante encontrar o ótimo exato, mas busca soluções muito próximas do ótimo global de forma eficiente.

---

## ⚙️ Hiperparâmetros Utilizados

Na implementação apresentada, foram utilizados os seguintes parâmetros:

- Tamanho da população: **40 morcegos**
- Número máximo de iterações: **150**
- Frequência mínima: **0.0**
- Frequência máxima: **2.0**
- Loudness inicial (A₀): **1.0**
- Taxa de pulso inicial (r₀): **0.1**

Esses parâmetros controlam o comportamento do algoritmo ao longo das iterações, regulando o equilíbrio entre exploração do espaço de busca e refinamento da solução.

---

## 🧪 Função Objetivo – Rastrigin

O algoritmo foi testado utilizando a **Função Rastrigin**, um problema clássico de otimização multimodal, conhecido por possuir diversos mínimos locais.

A escolha dessa função permite avaliar a capacidade do algoritmo de **escapar de mínimos locais**.

---

## ▶️ Como Executar o Algoritmo

### 1. Clonar o repositório
```bash
git clone https://github.com/SEU_USUARIO/bat-algorithm.git
