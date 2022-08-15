def limited_fib(n):
    sum = 0
    x, y = 1, 2

    while y < n:
        x, y = y, x + y
        if x % 2 == 0:
            sum += x
    return sum

print(limited_fib(4000000))