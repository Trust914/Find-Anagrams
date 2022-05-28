# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    # [assignment] Add your code here
    for letter_word in word:
        for letter_anagram in anagram:
            if not letter_word.isalpha() or not letter_anagram.isalpha():
                return "Invalid entry! The words can only contain letters of the alphabet."
    if word == "" or anagram == "":
        return "No word entered"
    else:
        lenght_of_word = len(word)
        lenght_of_anagram = len(anagram)

        for letters in anagram:
            count = word.count(letters)
            count2 = anagram.count(letters)
            if (count == count2) and (lenght_of_word == lenght_of_anagram):
                return True
            else:
                return False    

Word1 = input("Type the first word: \n").lower()
Word2 = input("Type the Second word: \n").lower()

print(find_anagram(Word1, Word2))