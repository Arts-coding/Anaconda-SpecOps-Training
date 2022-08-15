def selection_sort(numb):
    n = len(numb)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if numb[j] < numb[min_index]:
                min_index = j     
        
        numb[i], numb[min_index] = numb[min_index], numb[i]
    return numb

print(selection_sort([ 1, 5, 3, 9, 8,]))