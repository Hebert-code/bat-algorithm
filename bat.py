import numpy as np
from typing import Tuple, Callable
from dataclasses import dataclass

@dataclass
class BatSolution:
    position: np.ndarray
    fitness: float
    iteration: int

class BatOptimizer:
    def __init__(self, objective: Callable, dim: int = 2, bounds: Tuple[float, float] = (-5.12, 5.12),
                 n_bats: int = 50, max_iter: int = 200):
        self.objective = objective
        self.dim = dim
        self.lb, self.ub = bounds
        self.n_bats = n_bats
        self.max_iter = max_iter

        self.f_min, self.f_max = 0.0, 2.0
        self.alpha, self.gamma = 0.9, 0.9
        self.A0, self.r0 = 1.0, 0.1
        self.reset()

    def reset(self):
        self.positions = None
        self.velocities = None
        self.frequencies = None
        self.loudness = None
        self.pulse_rates = None
        self.fitness = None
        self.best_pos = None
        self.best_fitness = np.inf
        self.history = []

    def metodo1_inicializar_populacao(self):
        self.positions = np.random.uniform(self.lb, self.ub, (self.n_bats, self.dim))
        self.velocities = np.zeros((self.n_bats, self.dim))
        self.frequencies = np.random.uniform(self.f_min, self.f_max, self.n_bats)
        self.loudness = np.full(self.n_bats, self.A0)
        self.pulse_rates = np.full(self.n_bats, self.r0)

        self.fitness = np.array([self.objective(pos) for pos in self.positions])
        best_idx = np.argmin(self.fitness)
        self.best_pos = self.positions[best_idx].copy()
        self.best_fitness = self.fitness[best_idx]

    def metodo2_atualizar_frequencia(self):
        beta = np.random.random(self.n_bats)
        self.frequencies = self.f_min + (self.f_max - self.f_min) * beta

    def metodo3_atualizar_velocidade_posicao(self):
        for i in range(self.n_bats):
            direction = self.best_pos - self.positions[i]
            self.velocities[i] += self.frequencies[i] * direction
            self.positions[i] += self.velocities[i]
            self.positions[i] = np.clip(self.positions[i], self.lb, self.ub)

    def metodo4_busca_local(self):
        A_media = np.mean(self.loudness)
        for i in range(self.n_bats):
            if np.random.random() < self.pulse_rates[i]:
                epsilon = np.random.uniform(-1, 1, self.dim)
                local_pos = self.best_pos + epsilon * A_media
                self.positions[i] = np.clip(local_pos, self.lb, self.ub)

    def metodo5_aceitar_solucao(self, iteration: int):
        for i in range(self.n_bats):
            new_fitness = self.objective(self.positions[i])

            if (new_fitness < self.fitness[i] and np.random.random() < self.loudness[i]):
                self.fitness[i] = new_fitness
                self.loudness[i] *= self.alpha
                self.pulse_rates[i] = self.r0 * (1 - np.exp(-self.gamma * iteration))

                if new_fitness < self.best_fitness:
                    self.best_pos = self.positions[i].copy()
                    self.best_fitness = new_fitness

    def optimize(self):
        self.reset()
        self.metodo1_inicializar_populacao()

        for iteration in range(1, self.max_iter + 1):
            self.metodo2_atualizar_frequencia()
            self.metodo3_atualizar_velocidade_posicao()
            self.metodo4_busca_local()
            self.metodo5_aceitar_solucao(iteration)
            self.history.append(self.best_fitness)

        return BatSolution(self.best_pos.copy(), self.best_fitness, self.max_iter)

def rastrigin(x: np.ndarray) -> float:
    n = x.shape[-1]
    return 10*n + np.sum(x**2 - 10*np.cos(2*np.pi*x), axis=-1)

if __name__ == "__main__":
    otimizador = BatOptimizer(rastrigin, dim=2, n_bats=40, max_iter=150)
    solucao = otimizador.optimize()

    print("\n=== RESULTADO FINAL ===")
    print(f"Posição: [{solucao.position[0]:.6f}, {solucao.position[1]:.6f}]")
    print(f"Valor: {solucao.fitness:.6f}")

    eps = 1e-3
    if solucao.fitness < eps:
        print("✅ Mínimo global encontrado!")
    else:
        print("✅ Melhor solução encontrada (aproximação do mínimo global).")
