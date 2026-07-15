"""
448. Find All Numbers Disappeared in an Array (LeetCode)

Dado um vetor `nums` de n inteiros, onde cada nums[i] está no intervalo
[1, n], retorne todos os inteiros desse intervalo que NÃO aparecem em nums.

Exemplo:
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    n = 8, intervalo esperado = [1..8]
    saída = [5, 6]
"""

from typing import List


# Solução — Tempo: O(n) | Espaço: O(n)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        present = set(nums)
        return [number for number in range(1, len(nums) + 1) if number not in present]


if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(Solution().findDisappearedNumbers(nums))
