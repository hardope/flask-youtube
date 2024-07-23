from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

users = [
    {
        'name': 'Alice',
        'email': 'alice@gmail.com',
        'age': 20
    },
    {
        'name': 'Jarvis',
        'email': 'jarvis@outlook.com',
        'age': 16
    }
]

class User(Resource):

    def get(self):
        return users
    
    def post(self):
        data = request.json
        users.append(data)

        return {"message": "User Added"}

    def put(self):
        return {"message": "Got A PUT Request"}
    
api.add_resource(User, '/')

if __name__ == "__main__":
    app.run(debug=True)