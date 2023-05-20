#have a python dictionary having a key value pari representing word and  defintiion
#collects input form user, input is a word
#checks if a word is in a dictionry
#print defintiion

def main():
    word_dictionary = {
        "hi": "a way of greeting",
        "eyes": "an organ for seeing",
        "earth": "a planet in space",
    }
    
    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        if word in word_dictionary:
            print(word, ":", word_dictionary[word])

main()


#another version, install a py dictionary, type in a terminal:  pip install PyDictionary


from PyDictionary import PyDictionary

dictionary = PyDictionary()

while True:
    word = input("Enter your word: ")
    if word == "":
        break
      
    print(dictionary.meaning[word])


#another version, by making a list 

from PyDictionary import PyDictionary

dictionary = PyDictionary("eyes", "indentation", "head")

print(dictionary.getMeanings())
