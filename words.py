def print_upper_words(list_of_words):
    """ Prints out the upper case version of a list of words.

    print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])
    returns
    HELLO
    HEY
    GOODBYE
    YO
    YES
    """
    for word in list_of_words:
        print(word.upper())

def print_upper_words2(list_of_words):
    """ Prints out the upper case version of a list of words with only a specifc starting letter "h".

    print_upper_words2(["hello", "hey", "goodbye", "yo", "yes"])
    returns
    HELLO
    HEY
    """
    for word in list_of_words:
        if word.startswith("h") or word.startswith("H"):
            print(word.upper())

def print_upper_words3(list_of_words, starting_letter):
    """ Prints out the upper case version of a list of words with only a specifc starting letter of your choice.

    print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"], starting_letter=["Y"])
    returns
    YO
    YES
    """
    for word in list_of_words:
        for char in starting_letter:
            if word.startswith(char):
                print(word.upper())
                break

print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"], starting_letter=["y"])