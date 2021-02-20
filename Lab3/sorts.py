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
def mergesort_three(L):
    if len(L) <= 1:
        return L
    if len(L) <= 2: 
        if (L[0] <= L[1]):
            return L
        else: 
            temp = L[0]
            L[0] = L[1]
            L[1] = temp
            return L
    mid1 = len(L)//3
    mid2 = 2*(len(L)//3)
    left = L[:mid1]
    center = L[mid1:mid2]
    right = L[mid2:]
 
    mergesort_three(left)
    mergesort_three(center)
    mergesort_three(right)

    temp = merge_three(left, center, right)

    for i in range(len(temp)):
        L[i] = temp[i]
    return L


def merge_three(left, center, right): 
    L = []
    i = j = k = 0

    while i < len(left) or j < len(center) or k < len(right):
        if(i >= len(left) and j >= len(center)):
            L.append(right[k])
            k = k + 1
        elif(i >= len(left) and k >= len(right)):
            L.append(center[j])
            j = j + 1
        elif(j >= len(center) and k >= len(right)):
            L.append(left[i])
            i = i + 1
        elif(i >= len(left)):
            if (center[j] <= right[k]):
                L.append(center[j])
                j = j + 1
            else: 
                L.append(right[k])
                k = k + 1
        elif (j >= len(center)):
            if (left[i] <= right[k]):
                L.append(left[i])
                i = i + 1
            else: 
                L.append(right[k])
                k = k + 1
        elif (k >= len(right)):
            if (left[i] <= center[j]):
                L.append(left[i])
                i = i + 1
            else: 
                L.append(center[j])
                j = j + 1
        else:
            if(left[i] <= center[j] and left[i] <= right[k]):
                L.append(left[i])
                i = i + 1
            elif(right[k] <= center[j] and right[k] <= left[i]):
                L.append(right[k])
                k = k + 1 
            elif (center[j] <= left[i] and center[j] <= right[k]):
                L.append(center[j])
                j = j + 1
    return L