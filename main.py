# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if(sorted(word) == sorted(anagram)):
        print("True")
    else:
        print('False')

first_word = input('first_word: ')
second_word = input('second_word: ')
find_anagram(first_word, second_word)

