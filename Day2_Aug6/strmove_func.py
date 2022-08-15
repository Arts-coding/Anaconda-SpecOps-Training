def strmove_func(string, index):
    move_str = string[0:index + 1]
    string = string.replace(move_str, "")

    return string + move_str

print(strmove_func("hello", 2))

