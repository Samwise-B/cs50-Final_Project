import os

from hashlib import md5
from flask import Flask, flash, jsonify, redirect, render_template, request, session, url_for, send_from_directory, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash


from config.helpers import apology, login_required

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# Configure application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure SQLAlchemy URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///access.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Initialize Flask-SQLAlchemy
db = SQLAlchemy(app)

# Define Users data model
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # User authentication information.
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False, server_default='')

# Create the database and table
db.create_all()

# ensure filename has ALLOWED_EXTENSION
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# The Home page is accessible to anyone
@app.route('/')
def home_page():
    return render_template("index.html")

# About page for contact info and info about the project
@app.route('/about')
def about_page():
    return render_template("about.html")

# Page to search user database for a username input
@app.route("/admin", methods=["GET", "POST"])
def secret_page():
    if request.method == "GET":
        return render_template("secret.html")
    else:
        userInput = request.form.get("query")

        # ensure user has input something
        if not userInput:
            return apology("You must enter a username")

        # check for username in database
        result = db.engine.execute(f"SELECT * FROM users WHERE username='{userInput}'")
        # in order to use the data it must be fetched from the ResultProxy object
        rows = result.fetchall()

        if not rows:
            return apology("0 results found")

        return render_template("result.html", rows=rows[0])

# Level 3 flag input
@app.route("/flag", methods=["GET", "POST"])
@login_required
def flag_check():
    if request.method == "GET":
        return render_template("flag.html")
    else:
        # hashed flag to prevent cheating
        flagHash = 'pbkdf2:sha256:50000$lZnnfd9Y$22a7c6d699b1021aa862b8fa6712d9608044dd2c036c64053efea48c8b321cf8'

        if not check_password_hash(flagHash, request.form.get("flag")):
            return apology("The flag you entered is not correct. You can't guess it.")
        else:
            return render_template("game_over.html")

# Route to upload files
@app.route("/upload", methods=["GET", "POST"])
@login_required
def upload():
    if request.method == "GET":
        return render_template("upload.html")
    else:
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        # not securing filename
        if not request.form.get("name"):
            filename = file.filename
            check = allowed_file(filename)
        else:
            filename = request.form.get("name")
            check = True

        if file and check:
            path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(path)
            return redirect(url_for('uploaded', filename=filename))
        else:
            return apology("Bad file upload request. Try again.")

# returns uploaded file to user
@app.route('/uploads/<filename>')
@login_required
def uploaded(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Login page
@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    else:
        username = request.form.get("username")
        password = request.form.get("password")

        # ensure input was entered
        if not username or not password:
            return apology("You must enter a username and password")

        # query database for username
        user = Users.query.filter_by(username=username).first()

        # ensure username exists
        if not user:
            return apology("You must enter a valid username")

        # ensure password is correct
        inputHash = md5(password.encode()).hexdigest()

        if inputHash != user.password:
            return apology("You must enter a valid password")

        # create user session to remember user
        session["user_id"] = user.id

        return redirect("/")

@app.route("/logout")
def logout():
    """Log user out"""
    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)

# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)