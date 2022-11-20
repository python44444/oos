# これはルーティングのpython
import os
from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, login_user, login_required, logout_user
from database import User

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

app = Flask(__name__)

app.config["SECRET_KEY"] = os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return User.get(id=int(id))


@login_manager.unauthorized_handler
def unauthorizedid():
    return redirect("/login")


@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    return redirect("/")


@app.route("/admin_login")
def admin_login():
    return render_template("admin_login.html")


@app.route("/admin_logout")
@login_required
def admin_logout():
    return redirect("/")


@app.route("/signup")
def signup():
    return render_template("signup.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/upload")
def upload():
    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)
