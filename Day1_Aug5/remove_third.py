def remove_third(string):
    res = string[0]

    for i in range(0, len(string)):
        if i % 3 != 0:
            print(i)
            res += string[i]

    return res
string = "Enter string:"
print(remove_third(string))
