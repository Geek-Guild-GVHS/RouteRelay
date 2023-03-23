from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    school = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def login(name=None):
    correctPassword = None
    if request.method == "POST":
        passwordHash = db.session.execute(db.select(User).filter_by(email=request.form["Email"].lower())).scalar_one().password
        correctPassword = check_password_hash(passwordHash, request.form["Password"])

        if (correctPassword):
            return redirect("/home")

    return render_template("login.html", name=name, correctPassword=correctPassword)

@app.route('/register', methods=["GET", "POST"])
def register(name=None):
    if request.method == "POST":
        user = User(
            name = request.form["Name"].lower(),
            school = request.form["School"].lower(),
            email = request.form["Email"].lower(),
            password = generate_password_hash(request.form["Password"])
        )

        db.session.add(user)
        db.session.commit()

    return render_template("register.html", name=name)

@app.route('/home')
def home():
    return "Login Successful"


if __name__=="__main__":
    app.run(debug=True, port=8000)