# This function is my implementation of insertion sorted

def insertion_sort(a):
    if not a:
        return
    if len(a) == 1:
        return a

    for j in range(1,len(a)):
        key = a[j]
        for i in range(j-1,-1,-1):
            # exchange two elements in a
            if a[i] > key:
                a[i],a[i+1] = a[i+1],a[i] #change two elements position in python!!!!!!!!!
                i -= 1
            else:
                continue # if a[i] <= key, jump out of current loop

def insertion_sort2(a):
    if not a:
        return
    if len(a) == 1:
        return a

    for j in range(1,len(a)):
        key = a[j]
        i = j - 1
        while key < a[i] and i >= 0:
            tmp = a[i]
            a[i] = key
            a[i+1] = tmp
            i -= 1

# Test in this case
a = [3,5,1,2,6,4,9,100,3,4]
a1 = [1,3,4,2]
a2 = [10,9,8,7,6,5,4,3,2,1]
a3 = [100,-1,6,8,4,3,5,2,1,6,8,8,8,8,8,8,12]
print(insertion_sort2(a3) == insertion_sort(a3))
print(a3)
