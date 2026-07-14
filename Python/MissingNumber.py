"""
268. Missing Number (LeetCode)

Dado um vetor `nums` contendo n números distintos no intervalo [0, n],
retorne o único número desse intervalo que está faltando no vetor.

Exemplo:
    nums = [3, 0, 1]
    n = 3, intervalo esperado = [0, 1, 2, 3]
    saída = 2   # é o único número de 0..3 que não aparece em nums
"""

from typing import List


# ---------------------------------------------------------------------------
# Nível Júnior — Verificação direta com "in"
# ---------------------------------------------------------------------------
# Ideia: o intervalo completo é [0, n]. Basta percorrer cada número desse
# intervalo e checar se ele está no vetor. O primeiro que não estiver é a
# resposta. É a tradução mais literal do enunciado.
#
# Complexidade:
#   Tempo:  O(n^2) — para cada um dos n+1 números, o "in" percorre o vetor
#   Espaço: O(1)   — não usamos memória extra
class SolutionJunior:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for number in range(n + 1):
            if number not in nums:
                return number
        return -1  # nunca deve ocorrer, dado o enunciado


# ---------------------------------------------------------------------------
# Nível Pleno — Fórmula da soma de Gauss
# ---------------------------------------------------------------------------
# Ideia: a soma de todos os números de 0 a n é conhecida pela fórmula
# n*(n+1)/2. Se somarmos os elementos do vetor e subtrairmos da soma
# esperada, sobra exatamente o número que falta.
#
# Complexidade:
#   Tempo:  O(n) — uma única passada para somar o vetor
#   Espaço: O(1) — só guardamos dois números (soma esperada e soma real)
class SolutionPleno:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


# ---------------------------------------------------------------------------
# Nível Sênior — XOR (manipulação de bits)
# ---------------------------------------------------------------------------
# Ideia: fazendo XOR de cada índice (0..n) com cada valor do vetor, todo
# número que aparece nos dois lados se cancela (x ^ x == 0). Sobra apenas
# o número que não tem par, que é exatamente o que falta.
# Além de O(n)/O(1) como a solução por soma, evita risco de overflow em
# linguagens com inteiros de tamanho fixo (Java, C++), sendo a abordagem
# clássica considerada "ótima" para esse problema.
#
# Complexidade:
#   Tempo:  O(n) — uma única passada
#   Espaço: O(1) — apenas uma variável acumuladora
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = len(nums)
        for i, value in enumerate(nums):
            missing ^= i ^ value
        return missing


if __name__ == "__main__":
    nums = [3, 0, 1]

    print("Júnior:", SolutionJunior().missingNumber(nums))
    print("Pleno: ", SolutionPleno().missingNumber(nums))
    print("Sênior:", Solution().missingNumber(nums))
