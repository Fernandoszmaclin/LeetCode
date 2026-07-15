"""
1. Two Sum (LeetCode)

Dado um vetor de inteiros `nums` e um inteiro `target`, retorne os índices
dos dois números que somados resultam em `target`.

Pode assumir que existe exatamente uma solução, e o mesmo elemento não
pode ser usado duas vezes.

Exemplo:
    nums = [2, 7, 11, 15], target = 9
    saída = [0, 1]
"""

from typing import List


# Solução — Tempo: O(n) | Espaço: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {value: idx for idx, value in enumerate(nums)}

        for i, value in enumerate(nums):
            complement = target - value
            if complement in indices and indices[complement] != i:
                return [i, indices[complement]]
        return []


if __name__ == "__main__":
    nums, target = [2, 7, 11, 15], 9
    print(Solution().twoSum(nums, target))
