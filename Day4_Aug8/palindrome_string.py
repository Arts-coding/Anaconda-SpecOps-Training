def palindrome(string):
    new_str = string.strip().lower()
    ch = ""

    for i in new_str:
        if i.isalpha():
            ch += i

    str_list = ch.split()

    if str_list == str_list[::-1]:
        return True
    return False

print(palindrome("A man, a plan, a canal: Panama"))