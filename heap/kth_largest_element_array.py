# We can use the heap data structure to search for the kth largest element
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or len(nums) < k:
            return

        heaps = []
        for cnt in nums:
            if len(heaps) < k:
                heapq.heappush(heaps,cnt)
            else:
                if cnt > heaps[0]:
                    heapq.heappop(heaps)
                    heapq.heappush(heaps, cnt)
        return heaps[0]
