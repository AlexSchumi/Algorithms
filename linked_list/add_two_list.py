# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        if not l1 and l2:
            return l1
        elif not l2 and l1:
            return l2

        node = guard_node = ListNode(0)

        while l1 != null or l2 != null:
            sum = 0
            if l1 != null:
                sum += l1.val
                l1 = l1.next
            if l2 != null:
                sum += l2.val
                l2 = l2.next

            node.next = ListNode(sum%10) # set the next node
            sum = sum // 10

        if sum == 1:
            node.next = ListNode(1)
        return guard_node.next
