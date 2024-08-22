from flask import Flask, render_template, request, redirect, session
from flask_pymongo import PyMongo

app = Flask(__name__)
app.secret_key = "your_secret_key"

# Configuration
app.config["MONGO_URI"] = "mongodb+srv://preetikanadar05:preetikanadar05@cluster0.2bi5z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        user = mongo.db.users.find_one({"email": email})
        if user:
            return "Email already registered!"
        else:
            mongo.db.users.insert_one({
                "name": name,
                "email": email,
                "password": password
            })
            session['email'] = email
            return redirect('/')

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = mongo.db.users.find_one({"email": email, "password": password})
        if user:
            session['email'] = email
            return redirect('/')
        else:
            return "Login Failed. Invalid credentials!"

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/register_game', methods=['POST'])
def register_game():
    if 'email' in session:
        game = request.form['game']
        mongo.db.registrations.insert_one({
            "email": session['email'],
            "game": game
        })
        return "Game registration successful!"
    else:
        return "You must be logged in to register!"

if __name__ == "__main__":
    app.run(debug=True)
