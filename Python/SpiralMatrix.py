"""
54. Spiral Matrix (LeetCode)

Dada uma matriz `matrix` de m x n, retorne todos os elementos dela em
ordem espiral (sentido horário, de fora para dentro).

Exemplo:
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    saída = [1,2,3,6,9,8,7,4,5]
"""

from typing import List


# Solução — Tempo: O(m·n) | Espaço: O(m·n)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        matrix = [row[:] for row in matrix]
        result = []

        while matrix:
            result += matrix.pop(0)
            matrix = [list(row) for row in zip(*matrix)][::-1]

        return result


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(Solution().spiralOrder(matrix))
