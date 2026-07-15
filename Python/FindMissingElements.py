"""
3731. Find Missing Elements (LeetCode)

Você recebe um vetor `nums` de inteiros únicos. Originalmente, `nums`
continha todo inteiro dentro de um certo intervalo, mas alguns podem ter
sumido. O menor e o maior inteiro do intervalo original ainda estão
presentes em `nums`.

Retorne, em ordem crescente, todos os inteiros que estão faltando nesse
intervalo. Se nenhum estiver faltando, retorne uma lista vazia.

Exemplos:
    nums = [1, 4, 2, 5]  -> [3]
    nums = [7, 8, 6, 9]  -> []
    nums = [5, 1]        -> [2, 3, 4]
"""

from typing import List


# Solução — Tempo: O(n+R) | Espaço: O(n)
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        smallest, largest = min(nums), max(nums)
        present = set(nums)
        return [number for number in range(smallest, largest + 1) if number not in present]


if __name__ == "__main__":
    for nums in ([1, 4, 2, 5], [7, 8, 6, 9], [5, 1]):
        print(Solution().findMissingElements(list(nums)))
