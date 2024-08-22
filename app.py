from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient

app = Flask(__name__)
app.secret_key = 'preeti@05'

# MongoDB connection
client = MongoClient('mongodb+srv://preetikanadar05:preetikanadar05@cluster0.2bi5z.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client['sports_registration']

# Admin credentials
admin_user_id = 'preetikanadar05@gmail.com'

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        db.users.insert_one({'name': name, 'email': email, 'password': password})
        return redirect('/login')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = db.users.find_one({'email': email, 'password': password})
        if user:
            session['user_id'] = user['_id']
            return redirect('/events')
        else:
            return 'Login Failed'
    return render_template('login.html')

@app.route('/events')
def events():
    if 'user_id' in session:
        return render_template('events.html')
    return redirect('/login')

@app.route('/admin')
def admin():
    if 'user_id' in session:
        user_id = session['user_id']
        user = db.users.find_one({'_id': user_id})
        if user['email'] == admin_user_id:
            users = list(db.users.find())
            registrations = list(db.registrations.find())
            return render_template('admin.html', users=users, registrations=registrations)
    return redirect('/login')

@app.route('/register_game', methods=['POST'])
def register_game():
    if 'user_id' in session:
        game = request.form['game']
        user_id = session['user_id']
        db.registrations.insert_one({'user_id': user_id, 'game': game})
        return redirect('/events')
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
