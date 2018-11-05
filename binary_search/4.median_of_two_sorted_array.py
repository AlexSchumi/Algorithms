import sys
class Solution(object):
    """
    This is my implementation of median of two sorted array
    """

    """
    time complexity O()
    space complexity O()
    """

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        L1  R1
        4 | 6  8  9             cut1 : number of elements in left of cut in nums1
                 L2  R2
        1  2  3  7 | 10  12     cut2: number of elements in left of cut in nums2

        cutL = 0
        cutR = len(nums1)
        """
        l = len(nums1) + len(nums2)
        med = l // 2

        if len(nums1) >= len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        cut1 = 0
        cut2 = 0
        cutL = 0
        cutR = len(nums1) - 1

        while (cut1 <= len(nums1)):
            cut1 = (cutL + cutR) // 2
            cut2 = max(0, med - cut1)
            L1 = -sys.maxsize if cut1 == 0 else nums1[cut1 - 1]
            R1 = sys.maxsize if cut1 == 0 else nums1[cut1]
            L2 = -sys.maxsize if cut2 == 0 else nums2[cut2 - 1]
            R2 = sys.maxsize if cut2 == 0 else nums2[cut2]

            if (L1 > R2):
                cutR = cut1 - 1
            elif(L2 > R1):
                cutL = cut1 + 1
            else: # If we have satisfied all the conditions
                if l % 2 == 0:
                    return (max(L1, L2) + min(R1, R2)) / 2
                else:
                    return max(L1, L2)


print(Solution().findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
