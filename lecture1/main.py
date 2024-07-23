from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Jarvis"

@app.route('/test')
def test():
    return "<h1>This is a Test</h1>"

@app.route('/hello/<name>')
@app.route('/hello')
def hello(name="Jarvis"):
    pass

if __name__ == '__main__':
    app.run(debug=True)