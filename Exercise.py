
def j_max_2(number1, number2):
    if number1 > number2:
        return number1
    else:
        return number2

def j_max_3(number1, number2, number3):
    if number1 > number2:
        if number1 > number3:
            return number1
    elif number2 > number3:
        return number2
    else:
        return number3

def j_max (num_list):
    #smallest possible float number
    maximum = 2.2250738585072014e-308
    for num in num_list:
        if num > maximum:
            maximum = num
    return maximum


def length(string):
    try:
        x = 0
        while True:
            has_index = string[x]
            x += 1
    except IndexError:
        return x

def vowel(char):
    vowel_list = ['a','e','o','i','u']
    if char.lower() in vowel_list:
        return True
    else:
        return False

def swedishizing_words(string):
    swedish = []
    for char in string:
        if (vowel(char)) or (char == " "):
            swedish.append(char)
        else:
            swedish.append(char + "o" + char)

    return "".join(swedish)

def sum(*args):
    answer = 0
    for number in args:
        answer += number
    return answer

def multiply(*args):
    answer = 1
    for number in args:
        answer = answer * number
    return answer

def reverse(string):
    return string[::-1]

def is_palindrome(string):
    reverse_string = reverse(string)
    if string == reverse_string:
        return True
    else:
        return False

def is_member(value, list):
    for item in list:
        if value == item:
            return True
    return False

def overlapping(list1, list2):
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                return True
    return False

def generate_n_chars(char, multiplier):
    return char * multiplier

def histogram(*args):
    for item in args:
        print(generate_n_chars('*',item))

def map_word_len(word_list):
    len_list = list(map(lambda x: length(x),word_list))
    return len_list

def find_longest_word(word_list):
    return j_max(map_word_len(word_list))

def filter_long_words(word_list, size):
    filter_list = [word for word in word_list if length(word) > size]
    return filter_list

def sentence_palindrome(sentence):
    ignored_characters = ['.',',','!','?',' ']
    word_list = list(filter(lambda x: x not in ignored_characters, sentence.lower()))
    return is_palindrome(word_list)

def sentence_pangram(sentence):
    # 97 - 122
    alphabet_list = list(range(97,123))
    alphabet_list = [chr(char) for char in alphabet_list]
    [alphabet_list.remove(letter.lower()) for letter in sentence if letter.lower() in alphabet_list]
    if not alphabet_list:
        return True
    else:
        return False

def n_bottles_of_beer_on_the_wall(n):
    while n > 0:
        if n > 2:
            print("{0} bottles of beer on the wall, {0} bottles of beer.\nTake one down, pass it around, {1} bottles of beer on the wall.".format(n,n-1) )
        elif n > 1:
            print(
                "{0} bottles of beer on the wall, {0} bottles of beer.\nTake one down, pass it around, {1} bottle of beer on the wall.".format(
                    n, n - 1))
        else:
            print(
                "{0} bottle of beer on the wall, {0} bottle of beer.\nTake one down, pass it around, {1} bottles of beer on the wall.".format(
                    n, n - 1))
        n -= 1

def translate(sentence):
    swedish_dict = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
    translated_list = []
    sentence = list(sentence.lower().split())
    [translated_list.append(swedish_dict[word]) if word in swedish_dict else translated_list.append(word) for word in sentence]
    return " ".join(translated_list)

def char_frequency(sentence):
    char_dict = dict()
    for char in sentence:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict


import string

def ceaser_cypher(ROT):
    if ROT < 0:
        return dict(zip(string.ascii_letters,
                        string.ascii_lowercase[26 + ROT:] + string.ascii_lowercase[:26 + ROT] + string.ascii_uppercase[26 + ROT:] + string.ascii_uppercase[:26 + ROT]))
    else:
        return dict(zip(string.ascii_letters,
                        string.ascii_lowercase[ROT:] + string.ascii_lowercase[:ROT] + string.ascii_uppercase[ROT:] + string.ascii_uppercase[:ROT]))

def cypher_message(msg, ROT, cypher_message=True):
    msg_cypher = []
    if cypher_message:
        cypher_dict = ceaser_cypher(ROT)
    else:
        cypher_dict = ceaser_cypher(-ROT)
    for char in msg:
        if char in (string.punctuation) or (char in string.whitespace):
            msg_cypher.append(char)
        else:
            msg_cypher.append(cypher_dict[char])
    return ("".join(msg_cypher))


def make_3sg_form(word):
    endwith_list = ['o', 's', 'x', 'z', 'ch', 'sh']
    if word.endswith('y'):
        return "".join(word[:len(word) - 1] + 'ies')
    elif word.endswith(tuple(endwith_list)):
        return "".join(word + 'es')
    else:
        return "".join(word + 's')

def make_ing_form(word):
  vowels_list = ['a','e','i','o','u']
  if word.endswith('ie'):
    return word[:len(word)-2]+'ying'
  elif word.endswith('e') and (word not in ['see','bee', 'flee','knee']):
    return word[:len(word)-1]+'ing'
  elif ((word[len(word) - 1] not in vowels_list) and (word[len(word) - 2] in vowels_list) and (word[len(word) - 3] not in vowels_list)):
    return word+word[len(word)-1]+'ing'
  else:
    return word+'ing'

def word_len_list_map(word_list):
    # return list(map(lambda word: len(word),word_list))
    return [len(word) for word in word_list]

from functools import reduce


def j_reduce_max(list):
    return reduce(lambda x, y: max(x, y), list)

def find_longest_word_reduce(word_list):
  return len(reduce(lambda a, b: a if len(a) > len(b) else b, word_list))

def filter_long_words_filter(word_list, word_size):
  return list(filter(lambda x: len(x) > word_size, word_list))

def translate_dict(word_list):
    swed_translate_dict = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt",
                           "year": "år"}
    return " ".join([(swed_translate_dict[word]) if word in swed_translate_dict else word for word in word_list.split()])

def reading_file_sentence_palindrome(file_name):
  with open(file_name, 'r') as f:
    [print(line) for line in f if sentence_palindrome(line.strip())]

def reading_file_semordnilap(file_name):
    with open(file_name, 'r') as f:
        orig_list = [line.strip() for line in f]
        reverse_list = [line[::-1] for line in orig_list]
        [print(word) for word in reverse_list if word in orig_list]
        # will print out semodrnilap and also palindromes such as tacocat

from collections import Counter
from functools import reduce


def reading_file_char_freq(file_name):
    with open(file_name, 'r') as f:
        return (reduce(lambda x, y: Counter(x) + Counter(y), f))

def reading_file_hapax(file_name):
  hapax_list = []
  reapeted_list = []
  with open(file_name, 'r') as f:
    for line in f:
      for word in line.split():
        exclude = set(string.punctuation)
        word = ''.join(ch for ch in word if ch not in exclude).lower()
        if word not in hapax_list and word not in reapeted_list:
          hapax_list.append(word)
        elif word in hapax_list:
          hapax_list.remove(word)
          reapeted_list.append(word)
  return hapax_list

def reading_file_copy_over_plus_index(file_name):
  with open(file_name, 'r') as r, open('Copy_File.txt', 'w') as w:
    for i,line in enumerate(r):
      w.write("{}:{}".format(i,line))

def reading_file_average_word_len(file_name):
    #remove punctuation from the words
    with open(file_name, 'r') as r:
        sum, count = 0, 0
        for line in r:
            for word in line.split():
                exclude = set(string.punctuation)
                word = ''.join(ch for ch in word if ch not in exclude)
                sum += len(word)
                count += 1
        print(sum,count)
        return sum / count

import random


def guess_num_game():
    user_name = input("Hello, What is your name?")
    print("Well, {}, I am thinking of a number between 1 and 20".format(user_name))
    guess = random.randint(1, 20)
    user_guess_counter = 0
    user_guess = 0
    while True:
        user_guess_counter += 1
        try:
            user_guess = int(input("Take a guess."))
        except:
            print("That is not an intger! try again!")

        if user_guess == guess:
            print("Good job, {}! You guessed my number in {} guesses!".format(user_name, user_guess_counter))
            break
        elif user_guess > guess:
            print("Your guess is too high.")
        elif user_guess < guess:
            print("Your guess is too low.")
        else:
            print("Enter an intger!")

from random import shuffle, choice


def anagram_game(word_list):

    #word_list = ['dog', 'cat', 'mouse', 'cow']
    random_word = choice(word_list)
    shuffle_random_word = list(random_word)
    shuffle(shuffle_random_word)
    shuffle_random_word = "".join(shuffle_random_word)
    while True:
        print("Shuffled Word is {}".format(shuffle_random_word))
        guess = str(input("Guess what the word is."))
        if guess == random_word:
            print("Correct!")
            break
        else:
            print("Try again")

def Lingo(word_list):
    word = list(choice(word_list))
    prev_guess_word = []
    while True:
        guess_word = list(input('Clue: {}\n'.format("".join(prev_guess_word))))
        prev_guess_word = []
        if guess_word == word:
            print("Correct!")
            break

        for index, char in enumerate(guess_word):
            if char in word:
                if index < len(word) and word[index] == guess_word[index]:
                    prev_guess_word.append("[{}]".format(char))
                else:
                    prev_guess_word.append("({})".format(char))
            else:
                prev_guess_word.append(char)

import re


def sentence_splitter(file):
    with open(file, 'r') as text, open('paragraph_after_sentence_splitter', 'w') as new_text:
        regex1 = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s')
        new_text.write(re.sub(regex1, '.\n', text.readline()))

def create_anagram_list(file):
    anagram_list = {}
    with open(file, 'r') as word_list:
        for word in word_list:
            word = word.strip()
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word not in anagram_list:
                anagram_list[sorted_word] = [word]
            else:
                dict_list = anagram_list[sorted_word]
                dict_list.append(word)
                anagram_list[sorted_word] = dict_list
        return anagram_list


def find_anagrams(word, file):
    anagram_list = create_anagram_list(file)
    word = ''.join(sorted(word.lower()))
    if word in anagram_list:
        print(anagram_list[word])
    else:
        print("No anagrams found")

import random

def bracket_generator(num_of_brackets):
    brackets = ['[',']']
    return "".join([random.choice(brackets) for num in range(num_of_brackets)])

def bracket_balancer(text):
    stack = []
    accepted_brackets_left = ['[']
    accepted_brackets_right = [']']
    balanced = True
    print(text)
    for char in text:
        if char in  accepted_brackets_left:
            stack.append(char)
        elif char in accepted_brackets_right:
            if len(stack) > 0 and stack[-1] in accepted_brackets_left:
                stack.pop()
            elif len(stack) == 0:
                balanced = False
                break


    if not stack and balanced == True:
        return True
    else:
        pass
    return False

def word_list_gen(word_list):
    with open('pokemon.txt', 'w') as text:
        text.write(re.sub(r'\s',r'\n',word_list))

from string import ascii_lowercase
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
logging.debug('Start Of Program')


def letter_alphabet_dict(word_list, pos):
    alphabet_dict = {}
    for word in word_list:
        if word[pos] not in alphabet_dict:
            alphabet_dict[word[pos]] = [word]
        else:
            temp_dict_list = alphabet_dict[word[pos]]
            temp_dict_list.append(word)
            alphabet_dict[word[pos]] = temp_dict_list
    return alphabet_dict

def remove_word_from_all_dicts(word,dict1,dict2):
    first_char, last_char = word[0], word[-1]
    first_char_list = dict1[first_char]
    first_char_list.remove(word)
    dict1[first_char] = first_char_list
    last_char_list = dict2[last_char]
    last_char_list.remove(word)
    dict2[last_char] = last_char_list
    return dict1, dict2


def word_game(file_name):
    logging.debug('Start of word_game func')
    with open(file_name, 'r') as file_list:
        word_list = [word.strip() for word in file_list]
        current_word = random.choice(word_list)
        run_through_word_list = []
        run_through_word_list.append(current_word)

        logging.debug('Current word choice: ' + current_word)

        first_letter_alphabet_dict = letter_alphabet_dict(word_list,0)
        last_letter_alphabet_dict = letter_alphabet_dict(word_list, -1)
        first_letter_alphabet_dict, last_letter_alphabet_dict = remove_word_from_all_dicts(current_word,
                                                                                           first_letter_alphabet_dict,
                                                                                           last_letter_alphabet_dict)
        while True:
            try:
                next_word = random.choice(first_letter_alphabet_dict[current_word[-1]])
            except KeyError:

                return run_through_word_list
                break
            except IndexError:

                return run_through_word_list
                break
            first_letter_alphabet_dict, last_letter_alphabet_dict = remove_word_from_all_dicts(next_word,
                                                                                               first_letter_alphabet_dict,
                                                                                               last_letter_alphabet_dict)
            current_word = next_word
            run_through_word_list.append(current_word)

            logging.debug(first_letter_alphabet_dict)
            logging.debug(last_letter_alphabet_dict)

    logging.debug('End Program')

def longest_list_in_game(file_name):

    longest_list = []
    longest_length = 0
    for index in range(1000000):
        temp_list = word_game(file_name)
        if longest_length < len(temp_list):
            longest_list = temp_list
            longest_length = len(temp_list)

    print("Longest Length of List: ",longest_length)
    print("List:\n",longest_list)
    with open('Longest_list.txt', 'w') as file:
        strings = str("Longest Length of List: ",longest_length,"\nList:\n", longest_length)
        file.write("Longest Length of List: ")
        file.write(longest_length)
        file.write("\nList:\n")
        file.write(longest_length)


def alternade(word,file_name):

    from itertools import product


    anagram_list = create_anagram_list(file_name)
    def find_anagrams(word):
        word = ''.join(sorted(word.lower()))
        if word in anagram_list:
            return (anagram_list[word])

    products = list(product([1, 0], repeat=len(word)))
    first_half = ([[word[i] for i, e in enumerate(p) if e] for p in products])
    second_half = ([[word[i] for i, e in enumerate(p) if not e] for p in products])
    for index, first_word in enumerate(first_half):

        if len(first_word) > 1 and len(second_half[index]) > 1:
            first_half_ana = find_anagrams("".join(first_half[index]))
            second_half_ana = find_anagrams("".join(second_half[index]))
            if first_half_ana and second_half_ana:
                key_string_name = """ "{}" broken into "{}" & "{}" makes the follow anagrams \n1: {} \n2 :{}""".format(word, "".join(first_half[index]),
                                    "".join(second_half[index]), ", ".join(first_half_ana), ", ".join(second_half_ana))
                print(key_string_name)

alternade('waists','unixdict.txt')