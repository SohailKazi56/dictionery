import json
from difflib import get_close_matches

#get close matches lib is used to get the closest match and sequence matcher can also be used to get the ratio by using ratio function
# "#" is used for commenting or marking and '"""' is used for documenting.

data = json.load(open("dictionary.json"))

def translate(w):
    w = w.lower()   #to convert the word into lower case
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys()))>0:
        yn =  input("Did you mean %s instead ??? , press Y is yes or N if no : " %get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exists. Please double check it"
        else :
            return "we doesn't understand your entry"
    else:
        print("The word doesn't exist. Please double check the word")

word = input("Enter The Word :  ")

output = translate(word)
if type(output) == list:  # without this it will print every word letter by letter
    for item in output:
        print(item)
else:
    print(output)