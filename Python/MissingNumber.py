"""
268. Missing Number (LeetCode)

Dado um vetor `nums` contendo n números distintos no intervalo [0, n],
retorne o único número desse intervalo que está faltando no vetor.

Exemplo:
    nums = [3, 0, 1]
    n = 3, intervalo esperado = [0, 1, 2, 3]
    saída = 2
"""

from typing import List


# Solução — Tempo: O(n) | Espaço: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


if __name__ == "__main__":
    nums = [3, 0, 1]
    print(Solution().missingNumber(nums))
