from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    progress = [
        "HTML",
        "python",
        "Flask",
        "routing",
        "templates",
    ]
    user = {
        "name": "John Doe",
        "age": 30,
        "phone": "1234567890"
    }
    return render_template('home.html', context={
        "progress": progress,
        "user": user
    })

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)