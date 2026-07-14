"""
448. Find All Numbers Disappeared in an Array (LeetCode)

Dado um vetor `nums` de n inteiros, onde cada nums[i] está no intervalo
[1, n], retorne todos os inteiros desse intervalo que NÃO aparecem em nums.

Exemplo:
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    n = 8, intervalo esperado = [1..8]
    saída = [5, 6]   # únicos números de 1 a 8 que não aparecem em nums
"""

from typing import List


# ---------------------------------------------------------------------------
# Nível Júnior — Verificação direta com "in"
# ---------------------------------------------------------------------------
# Ideia: percorrer cada número do intervalo [1, n] e checar se ele aparece
# no vetor. Se não aparecer, ele entra na resposta. Tradução literal do
# enunciado.
#
# Complexidade:
#   Tempo:  O(n^2) — para cada um dos n números, o "in" percorre o vetor
#   Espaço: O(1)   — sem contar o vetor de saída
class SolutionJunior:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        missing = []
        for number in range(1, n + 1):
            if number not in nums:
                missing.append(number)
        return missing


# ---------------------------------------------------------------------------
# Nível Pleno — Conjunto (set) auxiliar
# ---------------------------------------------------------------------------
# Ideia: colocar todos os valores de nums em um set (checagem O(1)) e então
# percorrer o intervalo [1, n] verificando quais números não estão no set.
#
# Complexidade:
#   Tempo:  O(n) — uma passada para montar o set, outra para checar
#   Espaço: O(n) — o set guarda até n elementos
class SolutionPleno:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        present = set(nums)
        return [number for number in range(1, len(nums) + 1) if number not in present]


# ---------------------------------------------------------------------------
# Nível Sênior — Marcação in-place com sinal negativo
# ---------------------------------------------------------------------------
# Ideia: como todo valor está em [1, n], podemos usar o próprio vetor como
# "tabela de presença": para cada valor v encontrado, marcamos a posição
# (v - 1) como negativa (sem alocar memória extra). No final, os índices
# que continuarem positivos indicam números que nunca apareceram — o
# número que falta é (índice + 1).
#
# Complexidade:
#   Tempo:  O(n) — duas passadas simples pelo vetor
#   Espaço: O(1) — reaproveita o próprio vetor de entrada (fora a saída)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for value in nums:
            index = abs(value) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]

        missing = [i + 1 for i, value in enumerate(nums) if value > 0]

        # restaura o vetor original (boa prática, evita efeito colateral)
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return missing


if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]

    print("Júnior:", SolutionJunior().findDisappearedNumbers(list(nums)))
    print("Pleno: ", SolutionPleno().findDisappearedNumbers(list(nums)))
    print("Sênior:", Solution().findDisappearedNumbers(list(nums)))
