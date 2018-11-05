import collections
import heapq
class Solution(object):
    # This is my first implementation of this question; easy way to use hashmap and sort by values in python
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        cnt = {}
        for i in range(len(nums)):
            if nums[i] not in cnt:
                cnt[nums[i]] = 1
            else:
                cnt[nums[i]] += 1

        #return sorted(cnt.values(),reverse=True)
        return [key for (key, value) in sorted(cnt.items(), key=lambda x: x[1], reverse=True)][:k]

    def topKFrequent2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = collections.Counter(nums)
        print(counts)
        heap = []
        for key, cnt in counts.items():
            if len(heap) < k: # if we do not have k elements in heap, append it
                heapq.heappush(heap, (cnt, key))
            else:
                if heap[0][0] < cnt:
                    heapq.heappop(heap) # pop up the smallest number in heap
                    heapq.heappush(heap, (cnt, key)) # push this larger element in heap
        return [x[1] for x in heap]

print(Solution().topKFrequent2([1,3,1,2,2,1], k = 2))
