from main import keywords
import requests
import regex
from PyInquirer import prompt, print_json
from examples import *
from prompt_toolkit.validation import Validator, ValidationError

def insert(keyword):
    response = requests.post(rf'http://139.59.46.128:5000/insert?keyword={keyword}')
    return response.json()

def delete(keyword):
    response = requests.post(rf'http://139.59.46.128:5000/delete?keyword={keyword}')
    return response.json()

def search(keyword):
    response = requests.get(rf'http://139.59.46.128:5000/search?keyword={keyword}')
    return response.json()

def get_keywords(prefix = ""):
    if(prefix == ""):
        response = requests.get(rf'http://139.59.46.128:5000/keywords')
        return response.text
    response = requests.get(rf'http://139.59.46.128:5000/keywords?keyword={prefix}')
    return response.json()

class Keywordvalidate(Validator):
    def validate(self, document):
        keyword = document.text
        if keyword == "":
            raise ValidationError(message='Please enter keyword', cursor_position=len(document.text))
        if ' ' in keyword:
            raise ValidationError(message='Keyword cannot contain spaces', cursor_position=len(document.text))
        elif keyword.isupper():
            raise ValidationError(message='Keyword must be lower case', cursor_position=len(document.text))
        

questions = [
    {
        'type' : 'list',
        'name' : 'command',
        'message': 'Select command',
        'choices': ['help', 'insert', 'delete', 'search', 'search with prefix', 'keywords']

    },
]
answers = prompt(questions, style = custom_style_1)

if answers['command'] == 'help':
    print ("List of commands\n\nhelp               : displays this message\ninsert <keyword>   : inserts keyword to the trie\ndelete <keyword>   : deletes the keyword if found in the trie\nsearch <keyword>   : returns whether keyword is in the trie or not\nprefix <keyword>   : print all the words with keyword as prefix\ndisplay            : prints all the keywords in the trie\n")

elif answers['command'] == 'insert':
    questions2 = [
        {
        'type': 'input',
        'name': 'keyword',
        'message': 'Enter Keyword',
        'validate': Keywordvalidate
        },
    ]    
    answers2 = prompt(questions2, style = custom_style_1)
    keyword = answers2['keyword']
    x = insert(keyword)
    print(x['response'])
    
elif answers['command'] == 'delete':
    questions2 = [
        {
        'type': 'input',
        'name': 'keyword',
        'message': 'Enter Keyword',
        'validate': Keywordvalidate
        },
    ]    
    answers2 = prompt(questions2, style = custom_style_1)
    keyword = answers2['keyword']
    if search(keyword):
        x = delete(keyword)
        print(x['response'])
    else:
        print("keyword not found")

elif answers['command'] == 'search':
    questions2 = [
        {
        'type': 'input',
        'name': 'keyword',
        'message': 'Enter Keyword',
        'validate': Keywordvalidate
        },
    ]    
    answers2 = prompt(questions2, style = custom_style_1)
    keyword = answers2['keyword']
    x = search(keyword)
    print(x['response'])

elif answers['command'] == 'search with prefix':
    questions2 = [
        {
        'type': 'input',
        'name': 'keyword',
        'message': 'Enter Keyword',
        'validate': Keywordvalidate
        },
    ]    
    answers2 = prompt(questions2, style = custom_style_1)
    prefix = answers2['keyword']
    x = get_keywords(prefix)
    print(x['response'])
    
    
    





