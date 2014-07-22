# Created by Matt Ziegler

# Dictionary with keys of sorted words pointing to the words they can make.
word_hash_table = {}
# Words that have been found.
found_words = []
# Sorted words that have been solved.
solved_words = []

def read_file():
    """
    Reads contents of a dictionary text file (dictionary.txt). Each
    word is sorted alphabetically and used as a key in the word_hash_table.
    The key is used to reference an array with all of the words that have the same
    letters. For example, the key "dgo" will point to an array containing "dog" and "god".
    """
    dictionary_file = open("dictionary.txt", "r")
    lines = dictionary_file.readlines()
    for line in lines:
        line = line.lower()
        line = line.split("\n")
        word = line[0]
        # Copy the word into a list so that it can be sorted.
        sorted_word = list(word)
        sorted_word.sort()
        sorted_word = tuple(sorted_word)
        # If the key does not exist, create an array for the key.
        if not tuple(sorted_word) in word_hash_table:
            word_hash_table[sorted_word] = []
        # Add the word to the list of words for the key.
        word_hash_table[sorted_word].append(word)

def start_solve_word(word):
    """
    Gives a list of all words that word (or word's sub-words) can
    be jumbled into.
    :param word: The word to solve.
    """

    # Clear the found_words and solved_words arrays in case they have values
    # in them from the last word that was solved.
    del found_words[:]
    del solved_words[:]
    # Make the word lower case to help with matching.
    word = word.lower()
    # Sort the word so it can be looked up in the word_hash_table.
    sorted_word = list(word)
    sorted_word.sort()
    # Call the recursive function to solve the word.
    solve_word(sorted_word)

    print("Here are the possible words:")
    for found_word in found_words:
        print(found_word)

def solve_word(word):
    """
    Recursive algorithm to solve a sorted word. All matched
    words are stored in the solved_words array.
    :param word: The sorted word to solve
    """

    # Store this word in the solved_words array so that the word won't
    # be attempted to solve again.
    solved_words.append(word)
    word_key = tuple(word)
    if word_key in word_hash_table:
        matched_words = word_hash_table[word_key]

        # For all words that match, add the ones that weren't already found.
        # There really shouldn't be a situation where some of the words were
        # already and others were not though.
        for matched_word in matched_words:
            if not matched_word in found_words:
                found_words.append(matched_word)

    # If the word is greater than one character, attempt to solve any sub-words.
    if len(word) > 1:
        for i in range(0, len(word)):
            new_word = word[:i] + word[i+1:]
            # Only attempt to solve words that were not already solved.
            if not new_word in solved_words:
                solve_word(new_word)

def start():
    """
    Starts the user input cycle. After the user enters one word to solve,
    they are prompted whether or not they would like to continue. Only
    alpha words with no special characters can be entered by the user.
    """
    user_wants_out = False
    while not user_wants_out:
        word = raw_input("Enter a word to solve: ")
        # Make sure the word is alpha (no special characters or numbers) with at least one character.
        while not word.isalpha():
            word = raw_input("Please enter a single word with no special characters:")
        # Start solving the word.
        start_solve_word(word)
        user_option = raw_input("Do you want to solve another word? (Y or N): ")
        user_option.lower()
        if not "y" == user_option:
            print("Have a good one!")
            user_wants_out = True


read_file()
start()