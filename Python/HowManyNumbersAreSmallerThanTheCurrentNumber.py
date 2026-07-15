"""
1365. How Many Numbers Are Smaller Than the Current Number (LeetCode)

Dado um vetor `nums`, para cada nums[i] conte quantos números do vetor são
estritamente menores que ele. Retorne um vetor com essas contagens, na
mesma ordem de nums.

Restrições relevantes:
    2 <= nums.length <= 500
    0 <= nums[i] <= 100

Exemplo:
    nums = [8, 1, 2, 2, 3]
    saída = [4, 0, 1, 1, 3]
"""

from typing import List


# Solução — Tempo: O(n log n) | Espaço: O(n)
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        first_index = {}
        for index, value in enumerate(sorted_nums):
            if value not in first_index:
                first_index[value] = index

        return [first_index[value] for value in nums]


if __name__ == "__main__":
    for nums in ([8, 1, 2, 2, 3], [6, 5, 4, 8], [7, 7, 7, 7]):
        print(Solution().smallerNumbersThanCurrent(list(nums)))
