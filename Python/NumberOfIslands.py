"""
200. Number of Islands (LeetCode)

Dado um grid m x n de caracteres '1' (terra) e '0' (água), conte quantas
ilhas existem. Uma ilha é formada por terras conectadas horizontal ou
verticalmente (não diagonal), cercada por água.

Exemplo:
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"],
    ]
    saída = 3
"""

from collections import deque
from typing import List


# Solução — Tempo: O(m·n) | Espaço: O(min(m, n))
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    grid[r][c] = "0"
                    queue = deque([(r, c)])
                    while queue:
                        cr, cc = queue.popleft()
                        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nr, nc = cr + dr, cc + dc
                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                                grid[nr][nc] = "0"
                                queue.append((nr, nc))
        return count


if __name__ == "__main__":
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(Solution().numIslands(grid))
