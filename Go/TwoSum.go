/*
1. Two Sum (LeetCode)

Dado um vetor de inteiros `nums` e um inteiro `target`, retorne os índices
dos dois números que somados resultam em `target`.

Pode assumir que existe exatamente uma solução, e o mesmo elemento não
pode ser usado duas vezes.

Exemplo:
    nums = [2, 7, 11, 15], target = 9
    saída = [0, 1]
*/

package main

// Solução — Tempo: O(n) | Espaço: O(n)
func twoSum(nums []int, target int) []int {
	indices := make(map[int]int)

	for i, value := range nums {
		complement := target - value
		if j, ok := indices[complement]; ok {
			return []int{j, i}
		}
		indices[value] = i
	}
	return []int{}
}
