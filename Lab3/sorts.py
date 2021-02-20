#bottom-up mergesort implementation
def mergesort_bottom(L):
    windowSize = 1 
    arrLen = len(L)
    while (windowSize < arrLen):
        lo = 0 
        while (lo < arrLen - windowSize):
            merge_bottom(L, lo, lo + windowSize - 1, min(lo+(windowSize*2)-1, arrLen-1) )
            lo += 2 * windowSize
        windowSize += windowSize

def merge_bottom(L, start, mid, end):
    leftSize = mid - start + 1
    rightSize = end - mid
    Left = []
    Right = []
    i = 0
    j = 0
    while (i < leftSize):
        Left.append(L[start+i])
        i = i + 1
    while (j < rightSize):
        Right.append(L[mid+1+j])
        j = j + 1
    i = 0
    j = 0
    k = start

    while (i < leftSize and j < rightSize):
        if (Left[i] <= Right[j]):
            L[k] = Left[i]
            i = i + 1 
            k = k + 1
        else: 
            L[k] = Right[j]
            j = j + 1
            k = k + 1
    while (i < leftSize):
        L[k] = Left[i]
        i = i + 1
        k = k + 1
    while (j < rightSize):
        L[k] = Right[j]
        j = j + 1
        k = k + 1

#three-way mergesort implementation
def mergesort_three():
    return

def merge_three():
    return