def number_sequence(numb):
    sorted_numb = []

    for i in numb:
        sorted_numb.append(i**2)
    sorted_numb.sort()

    return sorted_numb

print(number_sequence([2, 5, 8, 4]))