"""
1. Two Sum (LeetCode)

Dado um vetor de inteiros `nums` e um inteiro `target`, retorne os índices
dos dois números que somados resultam em `target`.

Pode assumir que existe exatamente uma solução, e o mesmo elemento não
pode ser usado duas vezes.

Exemplo:
    nums = [2, 7, 11, 15], target = 9
    saída = [0, 1]   # nums[0] + nums[1] == 9
"""

from typing import List


# ---------------------------------------------------------------------------
# Nível Júnior — Força bruta
# ---------------------------------------------------------------------------
# Ideia: testar todo par (i, j) possível e verificar se a soma bate com o
# target. É a solução mais intuitiva: "tentar todas as combinações".
#
# Complexidade:
#   Tempo:  O(n^2) — um loop dentro do outro
#   Espaço: O(1)   — não usamos memória extra
class SolutionJunior:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


# ---------------------------------------------------------------------------
# Nível Pleno — Hash map em duas passadas
# ---------------------------------------------------------------------------
# Ideia: em vez de comparar cada par, guardamos os valores já vistos em um
# dicionário (valor -> índice). Numa segunda passada, para cada número
# verificamos se o "complemento" (target - nums[i]) já está no dicionário.
#
# Complexidade:
#   Tempo:  O(n) — duas passadas simples pelo vetor
#   Espaço: O(n) — dicionário guarda até n elementos
class SolutionPleno:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {value: idx for idx, value in enumerate(nums)}

        for i, value in enumerate(nums):
            complement = target - value
            if complement in indices and indices[complement] != i:
                return [i, indices[complement]]
        return []


# ---------------------------------------------------------------------------
# Nível Sênior — Hash map em uma única passada
# ---------------------------------------------------------------------------
# Ideia: mesma técnica do hash map, mas construímos o dicionário e
# verificamos o complemento ao mesmo tempo, em uma única passada.
# Isso evita percorrer o vetor duas vezes e retorna assim que encontra o par.
#
# Complexidade:
#   Tempo:  O(n) — uma única passada pelo vetor
#   Espaço: O(n) — dicionário guarda no máximo n elementos
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            complement = target - value
            if complement in seen:
                return [seen[complement], i]
            seen[value] = i
        return []


if __name__ == "__main__":
    nums, target = [2, 7, 11, 15], 9

    print("Júnior:", SolutionJunior().twoSum(nums, target))
    print("Pleno: ", SolutionPleno().twoSum(nums, target))
    print("Sênior:", Solution().twoSum(nums, target))
