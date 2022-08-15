def insertion_sort(numb):

    for i in range(1, len(numb)): 
        j = i
        
        while j > 0 and numb[j - 1] > numb[j]:
            numb[j], numb[j - 1] = numb[j - 1], numb[j]
            j -= 1

    return numb

print(insertion_sort([ 5, 1, 3, 2, 8,]))
