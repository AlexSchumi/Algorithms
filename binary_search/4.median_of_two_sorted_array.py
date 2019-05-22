import sys
class Solution(object):
    """
    This is my implementation of median of two sorted array based on cutting point
    """

    """
    time complexity O(log(min(m,n)))
    space complexity O(1)
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

        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        cut1 = 0
        cut2 = 0
        cutL = 0
        cutR = len(nums1)

        while (cut1 <= len(nums1)): # if we do not have return
            cut1 = (cutL + cutR) // 2
            cut2 = max(0, med - cut1)
            if (cut1 == 0 and cut2 == 0):
                return nums2[cut2]
            L1 = -sys.maxsize if cut1 == 0 else nums1[cut1 - 1]
            R1 = sys.maxsize if cut1 == len(nums1) else nums1[cut1]
            L2 = -sys.maxsize if cut2 == 0 else nums2[cut2 - 1]
            R2 = sys.maxsize if cut2 == len(nums2) else nums2[cut2]

            if (L1 > R2):
                cutR = cut1 - 1
            elif(L2 > R1):
                cutL = cut1 + 1
            else: # If we have satisfied all the conditions
                if l % 2 == 0:
                    return (max(L1, L2) + min(R1, R2)) / 2
                else:
                    return min(R1, R2)
                    
        # if we jump out of the while loop, which means cut1 >= len(nums1), so we make cut1 as len(nums1)
        cut1 = len(nums1)
        cut2 =  max(0, med - cut1)
        if l % 2 == 0:
            return (max(nums1[len(nums1)-1], nums2[cut2-1]) + min(sys.maxsize, nums2[cut2])) / 2
        else:
            return min(sys.maxsize, nums2[cut2])
    """
    This is my second solution of this question;
    """
    def findMedianSortedArrays2(self, nums1, nums2):
        return

print(Solution().findMedianSortedArrays(nums1 = [3], nums2 = [-2, -1]))
