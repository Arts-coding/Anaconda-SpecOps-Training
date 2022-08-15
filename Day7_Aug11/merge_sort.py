def merge_sort(numb):
    if len(numb) > 1:
        numb_left = numb[:len(numb) // 2]
        numb_right = numb[len(numb) // 2:]

        merge_sort(numb_left)
        merge_sort(numb_right)

        i = 0 
        j = 0
        k = 0

        while i < len(numb_left) and j < len(numb_right):
            if numb_left[i] < numb_right[j]:
                numb[k] = numb_left[i]
                i += 1
            else:
                numb[k] = numb_right[j]
                j += 1
            k += 1

        while i < len(numb_left):
            numb[k] = numb_left[i]
            i += 1
            k += 1
        
        while j < len(numb_right):
            numb[k] = numb_right[j]
            j += 1
            k += 1

    return numb

print(merge_sort([ 1, 5, 3, 2, 8, 4, 4]))