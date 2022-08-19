def sum_square_difference(n):
    sum = 0
    square = 0

    for i in range(1,n + 1):
        sum += i
        square += i**2

    return sum**2 - square
    
print(sum_square_difference(100))
