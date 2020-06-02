def SelectionSort(a):
    for i in range(0, len(a)-1):
        min = i
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a
arr = [1123, 1244, 1247, 214105, 1743, 176, 5719, 22, 25, 28]
print(SelectionSort(arr))