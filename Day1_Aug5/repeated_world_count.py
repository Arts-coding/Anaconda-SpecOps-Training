sample = open("sample.txt", "r").read().strip().split(' ')

def repeatedworld_count(sample):
    result = ""

    for i in sample:
        if i not in result:
            result += i + ' = ' + str(sample.count(i)) + '\n'
    
    return result

print(repeatedworld_count(sample))
