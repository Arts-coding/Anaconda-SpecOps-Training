def oddnumbers_count(n1, n2):
    res = 0

    for i in range(n1, n2 + 1):
        if i % 2 != 0:
            res += 1
    return res

print(oddnumbers_count(3, 11))
