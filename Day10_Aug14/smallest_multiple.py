def smallest_multiple():
    n = 20

    i = 1
    while i <= 20:
        if n % i == 0:
            print(n)
        else:
            n +=1
        i +=1
print(smallest_multiple())
