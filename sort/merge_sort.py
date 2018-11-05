
# This file is to practice merge_sort algorithm in python
# merge_sort is a recursive algorithm to sort arrays

def sort(a, lo, hi):
    """
    nums: a unsorted list
    rtype: sorted array
    """
    if hi <= lo:
        return
    mid = lo + (hi - lo) // 2 # check out for mid calculation
    sort(a, lo, mid)     # sort the left array
    sort(a, mid + 1, hi) # sort the right array
    merge(a, lo, mid, hi)

# merge sorted array function
def merge(a, lo, mid, hi):
    left = a[lo:mid+1]
    right = a[mid+1:hi+1]
    for k in range(lo, hi+1):
        if not left:
            a[k] = right.pop(0)
        elif not right:
            a[k] = left.pop(0)
        elif left[0] > right[0]:
            a[k] = right.pop(0)
        else:
            a[k] = left.pop(0)

def my_merge_sort(a):
    lo = 0
    hi = len(a) - 1
    sort(a, lo, hi)

seq = [2, 5, 8, 10, 2, 1, 3,9, 6, 12]
print(seq)
my_merge_sort(seq)
print(seq)
