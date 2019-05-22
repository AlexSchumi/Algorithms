# Definition for singly-linked list.
import heapq
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    """
    This is my own implementation for merge k sorted linkedlist;
    It has passed leetcode testing
    Time complexity: O(nmax(len(head)))
    Space complexity: O(n)
    """
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        res = self.mergeTwoLists2(lists[0], lists[1])
        cur = 2
        while cur < len(lists):
            res = self.mergeTwoLists2(res, lists[cur])
            cur += 1
        return res

    """
    This is divide conquer for this problem, we divide conquer the length of lists
    Time complexity: O(nlogK)
    Space complexity: O(n)
    """
    def mergeKLists2(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or len(lists) == 0:
            return None

        res = self.sort(lists, lo = 0, hi = len(lists) - 1)
        return res

    """
    This is helper function to sort two list
    """
    def sort(self, lists, lo, hi):
        if lo >= hi:
            return lists[lo] # this is just a function to make it divide to the lower level;
        mid = (hi - lo) // 2 + lo
        l1 =  self.sort(lists, lo, mid)
        l2 = self.sort(lists, mid + 1, hi)
        return self.mergeTwoLists2(l1, l2)

    """
    This is while loop implementation of merge two sorted linked list
    We can also use recursion to solve this problem
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
    This is priority queue(heapq) implementation in python
    Time complexity: O(nlogk)
    Space complexity: O(n)
    change it in python's pq
    """
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None
        res = cur = ListNode(0)
        queue = []
        for node in lists:
            queue.append((node.val, node))
        heapq.heapify(queue)
        while queue:
            val, cur.next = heapq.heappop(queue)
            cur = cur.next
            if cur.next:
                heapq.heappush(queue, (cur.next.val, cur.next))
        return res.next

l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l3 = ListNode(2)
l3.next = ListNode(6)
#print(Solution().mergeKLists([l1,l2,l3]))
