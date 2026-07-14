"""
3731. Find Missing Elements (LeetCode)

Você recebe um vetor `nums` de inteiros únicos. Originalmente, `nums`
continha todo inteiro dentro de um certo intervalo, mas alguns podem ter
sumido. O menor e o maior inteiro do intervalo original ainda estão
presentes em `nums`.

Retorne, em ordem crescente, todos os inteiros que estão faltando nesse
intervalo. Se nenhum estiver faltando, retorne uma lista vazia.

Exemplos:
    nums = [1, 4, 2, 5]  -> [3]              # intervalo [1..5]
    nums = [7, 8, 6, 9]  -> []                # intervalo [6..9], completo
    nums = [5, 1]        -> [2, 3, 4]         # intervalo [1..5]
"""

from typing import List


# ---------------------------------------------------------------------------
# Nível Júnior — Verificação direta com "in"
# ---------------------------------------------------------------------------
# Ideia: descobrir o menor e o maior valor de nums (eles delimitam o
# intervalo original). Depois, percorrer cada número desse intervalo e
# checar se ele aparece em nums. Tradução literal do enunciado.
#
# Complexidade (n = len(nums), R = tamanho do intervalo [menor, maior]):
#   Tempo:  O(n * R) — para cada número do intervalo, o "in" percorre nums
#   Espaço: O(1)      — sem contar a lista de saída
class SolutionJunior:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        smallest = min(nums)
        largest = max(nums)

        missing = []
        for number in range(smallest, largest + 1):
            if number not in nums:
                missing.append(number)
        return missing


# ---------------------------------------------------------------------------
# Nível Pleno — Conjunto (set) auxiliar
# ---------------------------------------------------------------------------
# Ideia: colocar os valores de nums em um set (checagem O(1) em média) e
# então percorrer o intervalo [menor, maior] filtrando os que não estão
# presentes.
#
# Complexidade:
#   Tempo:  O(n + R) — uma passada para montar o set, outra para o intervalo
#   Espaço: O(n)      — o set guarda até n elementos
class SolutionPleno:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        smallest, largest = min(nums), max(nums)
        present = set(nums)
        return [number for number in range(smallest, largest + 1) if number not in present]


# ---------------------------------------------------------------------------
# Nível Sênior — Vetor de presença (indexação direta, sem hashing)
# ---------------------------------------------------------------------------
# Ideia: como os valores são inteiros limitados ao intervalo [menor, maior],
# em vez de um hash set podemos usar uma lista de booleanos ("seen"), onde
# cada valor tem uma posição fixa (value - smallest). Marcar e consultar
# presença vira indexação direta de lista, mais rápida que calcular hash e
# sem colisões — a técnica típica de "counting/bucket" para valores
# limitados.
#
# Complexidade:
#   Tempo:  O(n + R) — uma passada para marcar, outra para coletar os faltantes
#   Espaço: O(R)      — vetor de presença do tamanho do intervalo
class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        smallest, largest = min(nums), max(nums)
        seen = [False] * (largest - smallest + 1)

        for value in nums:
            seen[value - smallest] = True

        return [smallest + i for i, found in enumerate(seen) if not found]


if __name__ == "__main__":
    for nums in ([1, 4, 2, 5], [7, 8, 6, 9], [5, 1]):
        print("Júnior:", SolutionJunior().findMissingElements(list(nums)))
        print("Pleno: ", SolutionPleno().findMissingElements(list(nums)))
        print("Sênior:", Solution().findMissingElements(list(nums)))
        print()
