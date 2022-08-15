def _numbers(n):
    sum = 0
    mult = 1

    while n != 0:
        sum += n % 10
        mult *= n % 10
        n = n // 10
    
    res = mult - sum
    return res

print(_numbers(25))
