from PyInquirer import prompt
from examples import *
from prompt_toolkit.validation import Validator, ValidationError
from api import *
import hashlib

correcthash = hashlib.sha256("hello".encode()).hexdigest()
print(correcthash)
triename = ""
loggedin = False

class Keywordvalidate(Validator):
    def validate(self, document):
        keyword = document.text
        if keyword == "":
            raise ValidationError(message='Please enter keyword', cursor_position=len(document.text))
        elif ' ' in keyword:
            raise ValidationError(message='Keyword cannot contain spaces', cursor_position=len(document.text))
        elif not keyword.islower():
            raise ValidationError(message='Keyword must be in lower case', cursor_position=len(document.text))

class TrieNameValidator(Validator):
    def validate(self, document):
        name = document.text
        if name == "":
            raise ValidationError(message='Please enter the trie name', cursor_position=len(document.text))
        elif ' ' in name:
            raise ValidationError(message='trie name cannot contain spaces', cursor_position=len(document.text))
        elif not name.islower():
            raise ValidationError(message='trie name must be in lower case', cursor_position=len(document.text))
        elif not authname(name):
            raise ValidationError(message='trie name not found, try again', cursor_position=len(document.text))

class TriePassValidator(Validator):
    def validate(self, document):
        password = document.text
        hashpass = hashlib.sha256(password.encode()).hexdigest()
        global triename
        global loggedin


        if password == "":
            raise ValidationError(message='Please enter the password', cursor_position=len(document.text))
        if not auth(triename, hashpass):            
            raise ValidationError(message='Incorrect password, try again', cursor_position=len(document.text))
        else:
            loggedin = True

class TrieNameValidator2(Validator):
    def validate(self, document):
        name = document.text
        if name == "":
            raise ValidationError(message='Please enter the trie name', cursor_position=len(document.text))
        elif ' ' in name:
            raise ValidationError(message='trie name cannot contain spaces', cursor_position=len(document.text))
        elif not name.islower():
            raise ValidationError(message='trie name must be in lower case', cursor_position=len(document.text))
        elif authname(name):
            raise ValidationError(message='trie name already in use, try again', cursor_position=len(document.text))

class TriePassValidator2(Validator):
    def validate(self, document):
        password = document.text
        hashpass = hashlib.sha256(password.encode()).hexdigest()
        global triename
        global loggedin


        if password == "":
            raise ValidationError(message='Please enter the password', cursor_position=len(document.text))        
        else:
            createtrie(triename, hashpass)
            loggedin = True


selectTrie = [
    {
        'type' : 'list',
        'name' : 'select',
        'message': 'Select command',
        'choices': ['Use existing trie', 'Create new trie']
    }
]

ans = prompt(selectTrie, style = custom_style_1)

if (ans['select'] == 'Use existing trie'):    
    auth1 = [
        {
            'type' : 'input',
            'name' : 'triename',
            'message':  'Trie name',
            'validate': TrieNameValidator,
        },
    ]
    auth2 = [
        {
            'type' : 'password',
            'name' : 'password',
            'message':  'password',
            'validate': TriePassValidator
        }
    ]

    auth1ans = prompt(auth1, style = custom_style_1)
    triename = auth1ans['triename']
    auth2ans = prompt(auth2, style = custom_style_1)

else:
    auth1 = [
        {
            'type' : 'input',
            'name' : 'triename',
            'message':  'Trie name',
            'validate': TrieNameValidator2,
        },
    ]
    auth2 = [
        {
            'type' : 'password',
            'name' : 'password',
            'message':  'password',
            'validate': TriePassValidator2
        }
    ]
    auth1ans = prompt(auth1, style = custom_style_1)
    triename = auth1ans['triename']
    auth2ans = prompt(auth2, style = custom_style_1)

while loggedin:
    
    questions = [
        {
            'type' : 'list',
            'name' : 'command',
            'message': 'Select command',
            'choices': ['help', 'insert', 'delete', 'delete all','search', 'prefix', 'keywords', 'exit']

        },
    ]
    answers = prompt(questions, style = custom_style_1)

    if answers['command'] == 'help':
        print ("List of commands\n\nhelp               : displays this message\ninsert <keyword>   : inserts keyword to the trie\ndelete <keyword>   : deletes the keyword if found in the trie\ndeleteall          : deletes all keywords\nsearch <keyword>   : returns whether keyword is in the trie or not\nprefix <keyword>   : print all the words with keyword as prefix\nkeywords           : prints all the keywords in the trie\n")

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

    elif answers['command'] == 'delete all':
        questions2 = [
            {
                'type': 'list',
                'name': 'confirm',
                'message': 'Are you sure?',
                'choices': ['NO', 'YES']
            }
        ]
        answers2 = prompt(questions2, style = custom_style_1)
        if answers2['confirm'] == 'YES':
            x = deleteall()
            print(x['response'])
        

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

    elif answers['command'] == 'prefix':
        questions2 = [
            {
            'type': 'input',
            'name': 'keyword',
            'message': 'Enter Keyword',
            'validate': Keywordvalidate
            },
        ]    
        answers2 = prompt(questions2, style = custom_style_1)
        questions3 = [
            {
            'type': 'list',
            'name': 'order',
            'message': 'Ascending/Descending',
            'choices': ['Ascending' ,'Descending']
            },
        ]   
        answers3 = prompt(questions3, style = custom_style_1)
    
    
        prefix = answers2['keyword']
        x = get_keywords(prefix)
        v = x['response']
        if v == None or len(v) == 0:
            print("No keywords were found")
        else:
            v.sort()
            if answers3['order'] == 'Descending' : v = v[::-1]
            print(f"List of keywords starting with {prefix}:")
            print(*v, sep = "\n")

    elif answers['command'] == 'keywords':
        questions2 = [
            {
            'type': 'list',
            'name': 'order',
            'message': 'Ascending/Descending',
            'choices': ['Ascending' ,'Descending']
            },
        ]   
        answers2 = prompt(questions2, style = custom_style_1) 
        x = get_keywords("")
        v = x['response']
        if v == None or len(v) == 0:
            print("No keywords were found")
        else:
            v.sort()
            if answers2['order'] == 'Descending' : v = v[::-1]
            print(f"List of keywords:")
            print(*v, sep = "\n")
    else:
        print("Bye, have a good day!")
        break

    print('\n\n')    
    
    





