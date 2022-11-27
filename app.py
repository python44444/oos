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


@app.route("/dashboard")
def dashboard():
    details = Cars.select()
    datas = []
    for detail in details:
        if detail.ODO == 0:
            # datas.append(detail.id)
            # datas.append(detail.use_date)
            # datas.append(detail.start_time)
            # datas.append(detail.ending_time)
            # datas.append(detail.task)
            # datas.append(detail.car_select)
            # datas.append(detail.ODO)
            datas.append(detail)
    return render_template("dashboard.html", datas=datas)


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
    member_select = request.form["member_select"]
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
        member_select=member_select,
        ODO=ODO,
        oil=oil,
        text=text,
    )


@app.route("/register_chinko", methods=["POST"])
def register_chinko():
    use_date = request.form["use_date"]
    start_time = request.form["start_time"]
    ending_time = request.form["ending_time"]
    # task = request.form["task"]
    car_select = request.form["car_select"]
    member_select = request.form["member_select"]
    ODO = request.form["ODO"]
    oil = request.form["oil"]
    text = request.form["text"]

    Cars.create(
        use_date=use_date,
        start_time=start_time,
        ending_time=ending_time,
        task="ちんこ",
        car_select=car_select,
        member_select=member_select,
        ODO=ODO,
        oil=oil,
        text=text,
    )
    return render_template("admin_login.html")


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


# uploed画像データベース
@app.route("/upload", methods=["POST"])
def upload_unko():
    yusou1 = request.form["yusou1"]
    kyuuzyo1 = request.form["kyuuzyo1"]
    kagaku1 = request.form["kagaku1"]
    tank1 = request.form["tank1"]
    suisou1 = request.form["suisou1"]
    hashigo1 = request.form["hashigo1"]
    shien1 = request.form["shien1"]
    dankouhou1 = request.form["dankouhou1"]
    rennraku11 = request.form["renraku11"]
    renraku10 = request.form["renraku10"]
    renraku1 = request.form["renraku1"]
    yobisekisai = request.form["yobisekisai"]
    danshirei1 = request.form["danshirei1"]
    danshirei20 = request.form["danshirei20"]
    kyuukyuu20 = request.form["kyuukyuu20"]
    tank20 = request.form["tank20"]

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
