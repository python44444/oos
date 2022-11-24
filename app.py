import os
from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, login_user, login_required, logout_user
from database import User
from PIL import Image
from ocr import display


from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

app = Flask(__name__)

app.config["SECRET_KEY"] = os.urandom(24)
# login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(id):
    return User.get(id=int(id))

@app.route("/signup")
def signup():
    return render_template("signup.html")


# アカウント登録→その後にログインで
@app.route("/signup", methods=["POST"])
def signup_post():
    name = request.form.get("name")
    password = request.form.get("password")
    generate_password = generate_password_hash(password, method="sha256")
    User.create(name=name, password=generate_password, title="title", body="body")
    return redirect("/login")




@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    name = request.form.get("name")
    password = request.form.get("passwd")
    user = User.get(name=name)
    if check_password_hash(user.password, password):
        login_user(user)
        # return redirect("/")
    return redirect("/admin_login")


@app.route("/upload")
@login_required
def upload():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
@login_required
def upload_post():
    file = request.files["file"]
    img = Image.open(file)
    img.save("static/images/image.jpeg")
    out = display("static/images/image.jpeg")
    return render_template("upload.html", distance=out)
    # return render_template("admin_login.html", outfile=file)


@app.route("/register")
def car_register():
    return render_template("register.html")


@login_manager.unauthorized_handler
def unauthorized():
    return redirect("/login")


@app.route("/")
@login_required
def index():
    return render_template("index.html")





@app.route("/admin_login")
def admin_login():
    return render_template("admin_login.html")




@app.route("/admin_logout")
@login_required
def admin_logout():
    return redirect("/")




# トップページにログアウトボタンを作成する。
@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return redirect("/login")


if __name__ == "__main__":
    app.run(host="5.0.0.1", debug=True)
