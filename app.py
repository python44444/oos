# これはルーティングのpython
from flask import Flask, render_template, redirect


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/logout")
def logout():
    return redirect("/")


@app.route("/admin_login")
def admin_login():
    return render_template("admin_login.html")


@app.route("/admin_logout")
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
