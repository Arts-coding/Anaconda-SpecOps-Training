sample = open("sample.txt", "r").readlines()
my_words = open("random_words.txt", "r").readlines()
new_words = open("sample.txt", "a")

def capitalize_file(new_str):
    """This function get new_str , capitalizes the first letters of all words in the text 
        and saves it to another file.

        Args:
            new_str (_string)
            my_words (_list)
            new_words (_txt) """

    for x in range(0, len(my_words)):
        new_str += my_words[x].title()

    new_words.write(new_str)

capitalize_file("")