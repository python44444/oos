import os

from flask import Flask
from flask import render_template
from flask import redirect
from flask import request


from flask_login import LoginManager
from flask_login import login_user
from flask_login import login_required
from flask_login import logout_user

# パスワードがそのままデータベースに入るで暗号化して開発者に見れないようにする
from werkzeug.security import generate_password_hash  # 暗号化
from werkzeug.security import check_password_hash  # 暗号化したものをもとに戻す

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
@login_required
def index():
    return render_template("index.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


# アカウント登録→その後にログインで
@app.route("/signup", methods=["POST"])
def register():
    name = request.form["name"]
    password = request.form["password"]
    User.create(name=name, password=password)  # アカウント名はそのままで
    generate_password = generate_password_hash(
        password, method="sha256"
    )  # パスワードは暗号化したものを入れる
    User.create(name=name, password=generate_password)
    return redirect("/login")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    name = request.form.get("name")
    password = request.form.get("passwd")
    user = User.get(name=name)
    # if user.password == password:
    #     login_user(user)

    #     return redirect("/")
    if check_password_hash(
        user.password, password
    ):  # 入力したパスワードは暗号化されているがUserは気にすることなくパスワードを使用できる（自動化）
        login_user(user)
        return redirect("/")  # 一致していればログイン
    return redirect("/login")  # ログインしていない場合は再入力


# トップページにログアウトボタンを作成する。
@app.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
