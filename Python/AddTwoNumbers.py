"""
2. Add Two Numbers (LeetCode)

Você recebe duas listas ligadas não vazias representando dois inteiros não
negativos. Os dígitos são armazenados em ordem inversa (a cabeça da lista é
o dígito menos significativo). Some os dois números e retorne a soma também
como uma lista ligada, na mesma ordem inversa.

Exemplo:
    l1 = [2,4,3]  (representa 342)
    l2 = [5,6,4]  (representa 465)
    saída = [7,0,8]  (representa 807)
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solução — Tempo: O(max(m, n)) | Espaço: O(max(m, n))
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            if total >= 10:
                carry, total = 1, total - 10
            else:
                carry = 0

            current.next = ListNode(total)
            current = current.next

        return dummy.next


def build_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def list_to_values(node):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values


if __name__ == "__main__":
    l1 = build_list([2, 4, 3])
    l2 = build_list([5, 6, 4])
    print(list_to_values(Solution().addTwoNumbers(l1, l2)))
