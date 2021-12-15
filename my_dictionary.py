import json
from difflib import get_close_matches          #if user enters a wrong word or a word close to required word this library helps in finding close matches 

data = json.load(open("data.json"))  #to open the json file in which the word and their meanings of dictionary are present already.    

def translate(word):           #defined a function to detect and change word to search in dictionary.
    
    word = word.lower()             #check if word is in small letters
    if word in data:
        return data[word]
    elif word.title() in data:            #check if word entered is a title i.e First letter capital and other small eg: Title
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]        #check if word is in small letters

    elif len(get_close_matches(word , data.keys())) > 0 :    # check length of entered word and if its 
                                                             # close to the word in dictionary and greater than 0

        print("did you mean %s instead : " %get_close_matches(word, data.keys())[0])
        decide = input("press y for yes or n for no : ")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return(" Wrong word !!! Enter a correct word : ")
        else:
            return("You have entered wrong input please enter just y or n : ")
    else:
        print("pugger your paw steps on wrong keys")



word = input("Enter the word you want to search : \n")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
