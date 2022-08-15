def symbols_count(my_file):
    symbols = "`~!@#$%^&*()_-+={[}]|\:;',<.>/?"
    count = 0

    for i in my_file:
        for j in range(0, len(i)):
            if i[j] in symbols:
                count += 1
    return count

my_file = open("random_file.txt", "r").readlines()
print(symbols_count(my_file))