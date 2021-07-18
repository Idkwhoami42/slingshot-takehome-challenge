from flask import Flask
from flask_restful import Api, Resource, reqparse
from trie import Trie

app = Flask(__name__)
api = Api(app)
trie = Trie()

class insert(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('keyword', type=str, help='keyword', required = True)
        args = parser.parse_args()
        keyword = args['keyword']
        
        trie.insert(keyword)
        return {'response':'successfully inserted'}

class delete(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('keyword', type=str, help='keyword', required = True)
        args = parser.parse_args()
        keyword = args['keyword']
        
        if (not trie.search(keyword)):
            return {'response': 'Keyword not found'}
        else:
            trie.erase(keyword)
            return {'response': 'successfully deleted'}

class search(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('keyword', type=str, required = True)
        args = parser.parse_args()
        keyword = args['keyword']
        if (trie.search(keyword)): return {'response': 'Found'}
        else: return {'response': 'Not found'}

class keywords(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('keyword', type=str, required = False)
        args = parser.parse_args()
        if(args['keyword'] == None):
            return {'response' : trie.get_keywords("")}
        else:
            return {'repsonse' : trie.get_keywords_with_prefix(args['keyword'])}
    
    
api.add_resource(insert, '/insert') 
api.add_resource(delete, '/delete')
api.add_resource(search, '/search')
api.add_resource(keywords, '/keywords')
if __name__ == '__main__':
    app.run()
