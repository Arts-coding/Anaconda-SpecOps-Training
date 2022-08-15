def last_word_len(string):
    new_str = string.strip().split(" ")
    res = len(new_str[-1])

    return res

print(last_word_len("   fly me   to   the moon  "))