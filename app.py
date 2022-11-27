import os
import datetime
from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, login_user, login_required, logout_user
from database import User, Cars, Photos
from PIL import Image

# from ocr import display

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


@app.route("/")
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
    details = Cars.select()
    datas = []
    for detail in details:
        if detail.ODO == 0:
            datas.append(detail)

    return render_template("admin_login.html", datas=datas)


# @app.route("/admin_login")
# def reservations():
#     details = Cars.select()
#     datas = []
#     for detail in details:
#         if detail.ODO == 0:
#             datas.append(detail)
#     return render_template("admin_login.html", datas=datas)


@app.route("/register", methods=["GET"])
def register():
    return render_template("register.html")


@app.route("/comfirm", methods=["POST"])
def comfirm():
    use_date = request.form["use_date"]
    start_time = request.form["start_time"]
    ending_time = request.form["ending_time"]
<<<<<<< HEAD
    car_select = request.form["car_select"]
    select = request.form["select"]
=======
    # task = request.form["task"]
    car_select = request.form["car_select"]
    member_select = request.form["member_select"]
>>>>>>> dd41efea4f62426c2d8bb247ca764d1e70dbc21c
    ODO = request.form["odo"]
    oil = request.form["oil"]
    text = request.form["text"]

    return render_template(
        "comfirm.html",
        use_date=use_date,
        start_time=start_time,
        ending_time=ending_time,
        task="terminating",
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
<<<<<<< HEAD
    car_select = request.form["car_select"]
    select = request.form["select"]
=======
    # task = request.form["task"]
    car_select = request.form["car_select"]
    member_select = request.form["member_select"]
>>>>>>> dd41efea4f62426c2d8bb247ca764d1e70dbc21c
    ODO = request.form["ODO"]
    oil = request.form["oil"]
    text = request.form["text"]

    Cars.create(
        use_date=use_date,
        start_time=start_time,
        ending_time=ending_time,
<<<<<<< HEAD
        task="",
=======
        task="terminating",
>>>>>>> dd41efea4f62426c2d8bb247ca764d1e70dbc21c
        car_select=car_select,
        member_select=member_select,
        ODO=ODO,
        oil=oil,
        text=text,
    )

    details = Cars.select()
    datas = []
    for detail in details:
        if detail.ODO == 0:
            datas.append(detail)

    return render_template("admin_login.html", datas=datas)


@app.route("/upload")
@login_required
def upload():
    return render_template("upload.html")


# 画像写す
# @app.route("/upload", methods=["POST"])
# def upload_get():
#     file = request.files["file"]
#     img = Image.open(file)
# img = img.resize((200, 200))
#     path = "static/images/image.jpeg"
#     img.save(path)
#     out = display(path)
#     return render_template("upload.html", distance=out, path=path)


<<<<<<< HEAD
# app.route("/register_chinko", methods=["POST"])


def register_chinko():
    use_date = request.form["use_date"]
    start_time = request.form["start_time"]
    endiing_time = request.form["endiing_time"]
    car_select = request.form["car_select"]
    select = request.form["select"]
    ODO = request.form["odo"]
    oil = request.form["oil"]
    text = request.form["text"]

    Cars.create(
        use_date=use_date,
        start_time=start_time,
        endiing_time=endiing_time,
        task="",
        car_select=car_select,
        select=select,
        ODO=ODO,
        oil=oil,
        text=text,
    )
    return render_template("uplord.html")


=======
>>>>>>> dd41efea4f62426c2d8bb247ca764d1e70dbc21c
# uploed画像データベース
@app.route("/upload", methods=["POST"])
def upload_unko():
    yusou1 = request.files["yusou1"]
    img1 = Image.open(yusou1)
    # img1.resize((200, 200))
    path1 = "static/images/image1.jpeg"
    img1.save(path1)

    kyuuzyo1 = request.files["kyuuzyo1"]
    img2 = Image.open(kyuuzyo1)
    # img2.resize((200, 200))
    path2 = "static/images/image2.jpeg"
    img2.save(path2)

    kagaku1 = request.files["kagaku1"]
    img3 = Image.open(kagaku1)
    # img3.resize((200, 200))
    path3 = "static/images/image3.jpeg"
    img3.save(path3)

    tank1 = request.files["tank1"]
    img4 = Image.open(tank1)
    # img4.resize((200, 200))
    path4 = "static/images/image4.jpeg"
    img4.save(path4)

    suisou1 = request.files["suisou1"]
    img5 = Image.open(suisou1)
    # img5.resize((200, 200))
    path5 = "static/images/image5.jpeg"
    img5.save(path5)

    hashigo1 = request.files["hashigo1"]
    img6 = Image.open(hashigo1)
    # img6.resize((200, 200))
    path6 = "static/images/image6.jpeg"
    img6.save(path6)

    shien1 = request.files["shien1"]
    img7 = Image.open(shien1)
    # img7.resize((200, 200))
    path7 = "static/images/image7.jpeg"
    img7.save(path7)

    dankouhou1 = request.files["dankouhou1"]
    img8 = Image.open(dankouhou1)
    # img8.resize((200, 200))
    path8 = "static/images/image8.jpeg"
    img8.save(path8)

    rennraku11 = request.files["renraku11"]
    img9 = Image.open(rennraku11)
    # img9.resize((200, 200))
    path9 = "static/images/image9.jpeg"
    img9.save(path9)

    renraku10 = request.files["renraku10"]
    img10 = Image.open(renraku10)
    # img10.resize((200, 200))
    path10 = "static/images/image10.jpeg"
    img10.save(path10)

    renraku1 = request.files["renraku1"]
    img11 = Image.open(renraku1)
    # img11.resize((200, 200))
    path11 = "static/images/image11.jpeg"
    img11.save(path11)

    yobisekisai = request.files["yobisekisai"]
    img12 = Image.open(yobisekisai)
    # img12.resize((200, 200))
    path12 = "static/images/image12.jpeg"
    img12.save(path12)

    danshirei1 = request.files["danshirei1"]
    img13 = Image.open(danshirei1)
    # img13.resize((200, 200))
    path13 = "static/images/image13.jpeg"
    img13.save(path13)

    danshirei20 = request.files["danshirei20"]
    img14 = Image.open(danshirei20)
    # img14.resize((200, 200))
    path14 = "static/images/image14.jpeg"
    img14.save(path14)

    kyuukyuu20 = request.files["kyuukyuu20"]
    img15 = Image.open(kyuukyuu20)
    # img15.resize((200, 200))
    path15 = "static/images/image15.jpeg"
    img15.save(path15)

    tank20 = request.files["tank20"]
    img16 = Image.open(tank20)
    # img16.resize((200, 200))
    path16 = "static/images/image16.jpeg"
    img16.save(path16)

    Photos.create(
        yusou1=path1,
        kyuuzyo1=path2,
        kagaku1=path3,
        tank1=path4,
        suisou1=path5,
        hashigo1=path6,
        shien1=path7,
        dankouhou1=path8,
        renraku11=path9,
        renraku10=path10,
        renraku1=path11,
        yobisekisai=path12,
        danshirei1=path13,
        danshirei20=path14,
        kyuukyuu20=path15,
        tank20=path16,
    )

    photo_datas = Photos.select()
    size = photo_datas
    photo_data = Photos.get(id=size)
    return render_template("car.html", photo_data=photo_data)


@app.route("/admin_logout")
@login_required
def admin_logout():
    return redirect("/")


@app.route("/")
@login_required
def index():
    current_time = datetime.datetime.now()
    return render_template("index.html", current_time=current_time)


# トップページにログアウトボタンを作成する。
@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return redirect("/login")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
