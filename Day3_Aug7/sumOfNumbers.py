def sum_of_numbs(n):
    sum1 = 0
    sum2 = 0
    
    for i in range(1,n):
        sum1 += i
        sum2 += i ** 2

    sum1 = sum1 ** 2
    res = sum1 - sum2

    return res

print(sum_of_numbs(5))