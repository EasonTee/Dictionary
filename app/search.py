from flask import json
import difflib
import os

def get_static_json_file(filename):
    url = os.path.join('E:\\Dictionary\\app', 'static', filename )
    return json.load(open(url))


# a dictionary app
def word_func(word): #function to find the match the word with its meaning. 
    content = get_static_json_file('data.json')   
    if word.lower() in content.keys(): #if user input big letter
        print (word.lower()+' >>')
        return content[word.lower()]
    
    elif word in content.keys(): #if user input name like USA
        print (word+' >>')
        return content[word]
        
    elif len(difflib.get_close_matches(word,content.keys()))>0: #if user typo
        yn=input('Do you mean "%s" instead? Enter Y for Yes and N for No:  '%difflib.get_close_matches(word,content.keys())[0])
        
        if yn.upper()=='Y':
            print (difflib.get_close_matches(word,content.keys())[0]+' >>')
            return content[difflib.get_close_matches(word,content.keys())[0]]
        
        elif yn.upper()=='N':
            return 'There is no such word, please try again'
        
        else:
            return 'Cannot understand what do you mean?'
        
    else:
         return 'There is no such word, please try again'
         
#user input and output

    
def output(word):    
    output=word_func(word) #load main function here
    if type(output)==list:
        for idx, item in enumerate(output):
            return str(idx+1)+".",item   
    else:
        return output        


