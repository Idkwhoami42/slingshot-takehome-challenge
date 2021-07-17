from flask import Flask
from flask_restful import Api, Resource, reqparse
import pwn

app = Flask(__name__)
api = Api(app)

keywords = []
trie = pwn.process("trie.exe")

class insert(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('keyword', type=str, help='keyword', required = True)
        args = parser.parse_args()

        
        print(keywords)
        return {'keyword': args['keyword']}

class delete(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('keyword', type=str, help='keyword', required = True)
        args = parser.parse_args()

        keywords.remove(args['keyword'])

class search(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('keyword', type=str, required = True)
        args = parser.parse_args()

        if (args['keyword'] in keywords): return {'found': True}
        else: return {'found': False}

class keywords(Resource):
    def get(self):
        return {'keywords':keywords}
    
api.add_resource(insert, '/insert') 
api.add_resource(delete, '/delete')
api.add_resource(search, '/search')

if __name__ == '__main__':
    app.run()
