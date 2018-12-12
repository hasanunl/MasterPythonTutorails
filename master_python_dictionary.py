#Import library
import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

#Loading the json data as python dictionary
#Try typing "type(data)" in terminal after executing first two line of this snippet
data = json.load(open("dictionary.json"))

#Function for retriving definition
def retrive_definition(word):
    word = word.lower()

    #Check for non existing words
    #1st elif: To make sure the program return the definition of words that start with a capital letter (e.g. Delhi, Texas)
    #2nd elif: To make sure the program return the definition of acronyms (e.g. USA, NATO)
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("Did you mean %s instead? [y or n]: " % get_close_matches(word, data.keys())[0])
        if (action == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        elif (action == "n"):
            return ("The word doesn't exist, yet.")
        else:
            return ("We don't understand your entry. Apologies.")
#Input from user
word_user = input("Enter a word: ")

#Retrive the definition using function and print the result
output = retrive_definition(word_user)

#If a word has more than one definition, print them recursively
if type(output) == list:
    for item in output:
        print("-",item)
#For words having single definition
else:
    print("-",output)


