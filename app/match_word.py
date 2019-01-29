import json
import difflib

class Dictionary():
    
    def __init__ (self,content):
        self.content = content # load json file
    
    # detect whether user input match with json's key
    def find_key(self,word):
        content = json.load(open(self.content))
        #if user enter capital letter
        if word.lower() in content:
            word = word.lower()
            return word
        
        #if user input name without capitalize
        elif word.capitalize() in content:
            word = word.capitalize()
            return word
        
    
    # function to match json key to return its values like normal words
    def match(self,word):
        content = json.load(open(self.content))
        return content[word]
    
    # when user typo or misspell 
    # function to use difflib to find the nearest word from the json key
    def close_match(self,word):
        content = json.load(open(self.content))
        return difflib.get_close_matches(word,content.keys())




         