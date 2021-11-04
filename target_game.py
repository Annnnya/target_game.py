from typing import List
import random
import string

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    res = []
    for i in range(3):
        res.append(random.sample(string.ascii_uppercase, k=3))
    return res


def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    with open(f, 'r') as word_dict:
        res = []
        for line in word_dict:
            line = line.strip()
            if 4<= len(line) <=9:
                lil_list = [] + letters
                fnd = True
                for i in line:
                    if i in lil_list:
                        lil_list.remove(i)
                    else:
                        fnd = False
                if fnd and not (letters[4] in lil_list):
                    res.append(line)
    return res


def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish.
    """
    usr_words = []
    while True:
        try:
            usr_words.append(input())
        except EOFError:
            break
    return usr_words


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    res = []
    lil_list = []+letters
    for word in user_words:
        if len(word) >= 4:
            fnd = True
            for i in word:
                if i in lil_list:
                    lil_list.remove(i)
                else:
                    fnd = False
            if fnd and not word in words_from_dict:
                    res.append(word)
    return res


def results():
    """
    main function of the program
    Результати гри це кількість 
    правильних слів, які ввів гравець, 
    всі можливі слова, 
    слова, які гравець пропустив, 
    слова, які ввів гравець і які відсутні у словнику.
    """
    with open('result.txt', 'w') as res_file:
        grid = generate_grid()
        print(grid)
        letter_list = []
        for i in grid:
            for j in grid:
                letter_list.append(j.lower())
        list_of_words = get_words('en', letter_list)
        usr_wrd = get_user_words()
        pure_user_words = get_pure_user_words(usr_wrd, letter_list, list_of_words)
        right_wrd = []
        for i in usr_wrd:
            if i in list_of_words:
                right_wrd.append(i)
        res_file.write(len(right_wrd))
        res_file.write(list_of_words)
        res_file.write(pure_user_words)
    