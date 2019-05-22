
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
        if not l1 and not l2:
            return None
        elif not l1 and l2:
            return l2
        elif not l2 and l1:
            return l1
            
        node = guard_node = ListNode(0) # create a node to return

        while l1 and l2: # when two node are not null
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        if l1 or l2:
            node.next = l1 or l2
        return guard_node.next

    """
    This is my implementation of merge two sorted linked List by Nov.7
    Time complexity: Q(min(m,n))
    Space complexity: O(n)
    Sometimes, we will need a guardnode to locate the head of linked list
    """
    def mergeTwoLists2(self, l1, l2):
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1

        # cuz we will go throught the node by node.next
        res = node = ListNode(0) # look at the reference in python and function
        while l1 and l2:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        if l1:
            node.next = l1
        if l2:
            node.next = l2
        return res.next
    """
    This is recursion implementation of merge method
    """
    def mergeTwoLists3(self, l1, l2):
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists3(l1.next, l2)
            return l1
        l2.next = self.mergeTwoLists3(l1, l2.next)
        return l2




l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(15)
l2.next.next.next.next = ListNode(20)
l3 = ListNode(5)
l4 = l1

node = Solution().mergeTwoLists3(l3, l4) # 1 2 4 5
while node:
    print(node.val)
    node = node.next
