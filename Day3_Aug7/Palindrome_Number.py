def palindrome_number(x):
    numb = str(x)

    if numb == numb[::-1]:
        return True
    return False
    
print(palindrome_number(123))

