"""
9. Palindrome Number (LeetCode)

Dado um inteiro `x`, retorne True se `x` é um palíndromo (lê-se igual de
trás para frente) e False caso contrário.

Exemplo:
    x = 121   -> True
    x = -121  -> False (o sinal de menos quebra a simetria)
    x = 10    -> False (seria "01" ao inverter, o que não é válido)
"""


# Solução — Tempo: O(log10 n) | Espaço: O(1)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted = 0
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x //= 10

        return x == reverted or x == reverted // 10


if __name__ == "__main__":
    for value in (121, -121, 10, 0, 12321, 12345):
        print(Solution().isPalindrome(value))
