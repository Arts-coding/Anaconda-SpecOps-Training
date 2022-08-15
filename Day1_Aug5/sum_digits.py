def sum_digits(numb):
    sum = 0

    while numb != 0:
        sum += numb %10
        numb = numb // 10

    return sum

print(sum_digits(15))