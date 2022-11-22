# これはルーティングのpython
from flask import Flask, render_template, redirect

# パスワードがそのままデータベースに入るで暗号化して開発者に見れないようにする
from werkzeug.security import generate_password_hash  # 暗号化
from werkzeug.security import check_password_hash  # 暗号化したものをもとに戻す

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


@app.route("/logout")
def logout():
    return redirect("/login")


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

print("テスト")
