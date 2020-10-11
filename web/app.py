from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from pymongo import MongoClient


app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://db:27017")
db = client.aNewDB
UserNum = db['UserNum']
UserNum.insert({
    'num_of_users':0
    
})
class Visit(Resource):
    def get(self):
        prev_num = UserNum.find({})[0]['num_of_users']
        new_num = prev_num + 1
        UserNum.update({}, {"$set":{"num_of_users":new_num}})
        return str("Hello user" + str(new_num))

@app.route('/')
def hello_world():
    return 'hi'



@app.route('/b')
def hello():
    
    recJson={
        'f1':'abc',
        'f2':'asf'
    }
    return jsonify(recJson)

api.add_resource(Visit,"/hello")

if __name__=="__main__":
    app.run('0.0.0.0')