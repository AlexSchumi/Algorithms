# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    This is my first implementation of swap two nodes in linked list
    Time complexity: O(n)
    Space complexity: O(1)
    There is bug in my first version until I add cur.next = head when head is none.
    """
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        res = cur = ListNode(0) # set up a ancillary node for results

        while head.next: # if we had head.next node
            cur.next, tmp = head.next, head.next.next
            # tmp = head.next.next # tmp node to memory continue node
            cur = cur.next
            cur.next = head
            cur = cur.next
            head = tmp
            if not head:
                #print('Yes')
                #cur.next = head # why do I have to add this line, bug in my first try
                #return res.next
                break
        cur.next = head
        return res.next
        #return res.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
l1.next.next.next.next.next = ListNode(6)
res = Solution().swapPairs(l1)
a = []
while res:
    a.append(res.val)
    #print(a)
    res = res.next
print(a)
