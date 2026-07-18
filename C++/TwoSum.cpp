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

#include <unordered_map>
#include <vector>

using namespace std;

// Solução — Tempo: O(n) | Espaço: O(n)
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> indices;

        for (int i = 0; i < (int)nums.size(); i++) {
            int complement = target - nums[i];
            if (indices.count(complement)) {
                return {indices[complement], i};
            }
            indices[nums[i]] = i;
        }
        return {};
    }
};