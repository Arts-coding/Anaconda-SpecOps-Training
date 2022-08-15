from collections import Counter

def repeat_count(my_dict):
  
    return Counter(my_dict.values())

my_dict = {'a': 0, 'b': 4, 'c': 0, 'd': 0}
print(repeat_count(my_dict))