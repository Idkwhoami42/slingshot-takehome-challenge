import hashlib
from flask import Flask
from flask_restful import Api, Resource, reqparse
import hashlib
from trie import Trie

app = Flask(__name__)
api = Api(app)
tries = [
    {
        'name': 'default',
        'password': hashlib.sha256('slingshot'.encode()).hexdigest(),
        'trie': Trie()
    }
]
index = 0

class insert(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('keyword', type=str, help='keyword', required = True)
        args = parser.parse_args()
        keyword = args['keyword']
        
        tries[index]['trie'].insert(keyword)
        return {'response':'successfully inserted'}

class delete(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('keyword', type=str, help='keyword', required = True)
        args = parser.parse_args()
        keyword = args['keyword']
        
        if (not tries[index]['trie'].search(keyword)):
            return {'response': 'Keyword not found'}
        else:
            tries[index]['trie'].erase(keyword)
            return {'response': 'successfully deleted'}

class deleteall(Resource):
    def post(self):
        tries[index]['trie'].eraseall()
        return {'response' : 'successfully deleted all keywords'}

class search(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('keyword', type=str, required = True)
        args = parser.parse_args()
        keyword = args['keyword']
        if (tries[index]['trie'].search(keyword)): return {'response': 'Found'}
        else: return {'response': 'Not found'}

class keywords(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('keyword', type=str, required = False)
        args = parser.parse_args()
        if(args['keyword'] == None):
            return {'response' : tries[index]['trie'].get_keywords("")}
        else:
            return {'response' : tries[index]['trie'].get_keywords_with_prefix(args['keyword'])}

class auth(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type = str, required = True)
        parser.add_argument('pass', type = str, required = True)
        args = parser.parse_args()
        name = args['name']
        passw = args['pass']
        global index
        correctpass =  False
        for i in range(len(tries)):
            details = tries[i]
            if details['name'] == name and details['password'] == passw:
                index = i                
                correctpass = True
                break
        if correctpass:
            return {'response' : 'True'}
        else:
            return {'response' : 'False'}

class authname(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type = str, required = True)
        args = parser.parse_args()
        name = args['name']
        correctname = False
        for details in tries:
            if details['name'] == name:
                correctname = True
                break
        print('called', name)
        if correctname:
            return {'response' : 'True'}
        else:
            return {'response' : 'False'}

class createtrie(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type = str, required = True)
        parser.add_argument('pass', type = str, required = True)
        args = parser.parse_args()
        name = args['name']
        passw = args['pass']
        global index 
        tries.append({
            'name':name,
            'password':passw,
            'trie': Trie()
        })
        index = len(tries) - 1
        return {'response' : 'successfully createed'}



                
    
api.add_resource(insert, '/insert') 
api.add_resource(delete, '/delete')
api.add_resource(deleteall, '/deleteall')
api.add_resource(search, '/search')
api.add_resource(keywords, '/keywords')
api.add_resource(auth, '/auth')
api.add_resource(authname, '/authname')
api.add_resource(createtrie, '/createtrie')


if __name__ == '__main__':
    
    app.run("0.0.0.0")
