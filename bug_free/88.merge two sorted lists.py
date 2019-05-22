class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new = head = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                new.next = l1
                l1 = l1.next
            else:
                new.next = l2
                l2 = l2.next
            new = new.next

        while l1:
            new.next = l1
            l1 = l1.next
            new = new.next

        while l2:
            new.next = l2
            l2 = l2.next
            new = new.next

        return head.next
