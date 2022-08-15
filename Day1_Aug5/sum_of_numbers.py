my_numbers = open("random_numbers.txt", "r").readlines()

def sum_of_numbers(sum):
    """This function get my_numbers and return sum of numbers in txt file
        Args:
            sum (_int)
            my_numbers (_list)"""

    for i in my_numbers:
        number = i
        sum += int(number)
    return sum

print(sum_of_numbers(0))