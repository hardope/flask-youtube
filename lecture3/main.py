from flask import Flask, jsonify, request

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == "POST":
        
        data = request.json
        users.append(data)

        return jsonify({"message": "User Added"})

    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)