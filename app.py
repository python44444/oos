import os
from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, login_user, login_required, logout_user
from database import User, Cars
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


@login_manager.unauthorized_handler
def unauthorized():
    return redirect("/login")


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


@app.route("/login_user", methods=["POST"])
def login_post():
    name = request.form["name"]
    password = request.form["password"]
    user = User.get(name=name)
    if check_password_hash(user.password, password):
        login_user(user)

        # return redirect("/")
    return redirect("/admin_login")


@app.route("/admin_login")
@login_required
def admin_login_post():
    return render_template("admin_login.html")


@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")


@app.route("/comfirm", methods=["POST"])
def comfirm():
    use_date = request.form["use_date"]
    start_time = request.form["start_time"]
    ending_time = request.form["ending_time"]
    # task = request.form["task"]
    car_select = request.form["car_select"]
    select = request.form["select"]
    ODO = request.form["odo"]
    oil = request.form["oil"]
    text = request.form["text"]

    return render_template(
        "comfirm.html",
        use_date=use_date,
        start_time=start_time,
        ending_time=ending_time,
        task="ちんこ",
        car_select=car_select,
        select=select,
        ODO=ODO,
        oil=oil,
        text=text,
    )


@app.route("/register_chinko", methods=["POST"])
def register_chinko():
    use_date = request.form["use_date"]
    start_time = request.form["start_time"]
    endiing_time = request.form["endiing_time"]
    # task = request.form["task"]
    car_select = request.form["car_select"]
    select = request.form["select"]
    ODO = request.form["odo"]
    oil = request.form["oil"]
    text = request.form["text"]

    Cars.create(
        use_date=use_date,
        start_time=start_time,
        endiing_time=endiing_time,
        task="ちんこ",
        car_select=car_select,
        select=select,
        ODO=ODO,
        oil=oil,
        text=text,
    )
    return render_template("admin_login.html")


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


@app.route("/admin_logout")
@login_required
def admin_logout():
    return redirect("/")


@app.route("/")
@login_required
def index():
    return render_template("index.html")


# トップページにログアウトボタンを作成する。
@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return redirect("/login")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
