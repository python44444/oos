import os
from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, login_user, login_required, logout_user
from database import User, Cars, Photos
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
    return render_template("uplord.html")


@app.route("/upload")
@login_required
def upload():
    return render_template("upload.html")


# 画像写す
@app.route("/upload", methods=["POST"])
def upload_get():
    file = request.files["file"]
    img = Image.open(file)
    img = img.resize((200, 200))
    path = "static/images/image.jpeg"
    img.save(path)
    out = display(path)
    return render_template("upload.html", distance=out, path=path)


app.route("/register_chinko", methods=["POST"])


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
    return render_template("uplord.html")


# uploed画像データベース
@app.route("/upload", methods=["POST"])
def uplord_unko():
    yusou1 = request.form["yusou1"]
    img = Image.open(yusou1)
    img = img.resize((200, 200))
    path = "static/images/image1.jpeg"
    img.save(path)

    kyuuzyo1 = request.form["kyuuzyo1"]
    img = Image.open(kyuuzyo1)
    img = img.resize((200, 200))
    path = "static/images/image2.jpeg"
    img.save(path)

    kagaku1 = request.form["kagaku1"]
    img = Image.open(kagaku1)
    img = img.resize((200, 200))
    path = "static/images/image3.jpeg"
    img.save(path)

    tank1 = request.form["tank1"]
    img = Image.open(tank1)
    img = img.resize((200, 200))
    path = "static/images/image4.jpeg"
    img.save(path)

    suisou1 = request.form["suisou1"]
    img = Image.open(suisou1)
    img = img.resize((200, 200))
    path = "static/images/image5.jpeg"
    img.save(path)
    hashigo1 = request.form["hashigo1"]
    img = Image.open(hashigo1)
    img = img.resize((200, 200))
    path = "static/images/image6.jpeg"
    img.save(path)
    shien1 = request.form["shien1"]
    img = Image.open(shien1)
    img = img.resize((200, 200))
    path = "static/images/image7.jpeg"
    img.save(path)
    dankouhou1 = request.form["dankouhou1"]
    img = Image.open(dankouhou1)
    img = img.resize((200, 200))
    path = "static/images/image8.jpeg"
    img.save(path)
    rennraku11 = request.form["renraku11"]
    img = Image.open(renraku11)
    img = img.resize((200, 200))
    path = "static/images/image9.jpeg"
    img.save(path)
    renraku10 = request.form["renraku10"]
    img = Image.open(renraku10)
    img = img.resize((200, 200))
    path = "static/images/image10.jpeg"
    img.save(path)
    renraku1 = request.form["renraku1"]
    img = Image.open(renraku1)
    img = img.resize((200, 200))
    path = "static/images/image11.jpeg"
    img.save(path)
    yobisekisai = request.form["yobisekisai"]
    img = Image.open(yobisekisai)
    img = img.resize((200, 200))
    path = "static/images/image12.jpeg"
    img.save(path)
    danshirei1 = request.form["danshirei1"]
    img = Image.open(danshirei1)
    img = img.resize((200, 200))
    path = "static/images/image13.jpeg"
    img.save(path)
    danshirei20 = request.form["danshirei20"]
    img = Image.open(danshirei20)
    img = img.resize((200, 200))
    path = "static/images/image14.jpeg"
    img.save(path)
    kyuukyuu20 = request.form["kyuukyuu20"]
    img = Image.open(kyuuzyo1)
    img = img.resize((200, 200))
    path = "static/images/image15.jpeg"
    img.save(path)
    tank20 = request.form["tank20"]
    img = Image.open(tank1)
    img = img.resize((200, 200))
    path = "static/images/image16.jpeg"
    img.save(path)

    Photos.create(
        yusou1=yusou1,
        kyuuzyo1=kyuuzyo1,
        kagaku1=kagaku1,
        tank1=tank1,
        suisou1=suisou1,
        hashigo1=hashigo1,
        shien1=shien1,
        dankouhou1=dankouhou1,
        rennraku11=rennraku11,
        renraku10=renraku10,
        renraku1=renraku1,
        yobisekisai=yobisekisai,
        danshirei1=danshirei1,
        danshirei20=danshirei20,
        kyuukyuu20=kyuukyuu20,
        tank20=tank20,
    )
    return render_template("upload.html")


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
    app.run(host="0.0.0.0", port=5001, debug=True)
