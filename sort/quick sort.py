def quicksort(L, lo, hi):
    if lo < hi:
        p = partition(L, lo, hi)
        quicksort(L, lo, p-1)
        quicksort(L, p+1, hi)


def partition(L, lo, hi):
    pivot = L[hi]
    i = 0
    for j in range(hi):
        if L[j] <= pivot:
            L[j], L[i] = L[i], L[j]
            i += 1

    L[hi], L[i] = L[i], L[hi]
    return i # return pivot index

if __name__ == "__main__":
    L = [5,4,2,7,9,0,3]
    lo = 0
    hi = len(L) - 1
    quicksort(L, lo, hi)
    print(L)
