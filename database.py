# これデータベースpythonね
from playhouse.db_url import connect
from peewee import Model, IntegerField, CharField, TextField, TimestampField
from flask_login import UserMixin

# from dotenv import load_dotenv

# .envの読み込み
# load_dotenv()
# 実行したSQLをログで出力する設定


# データベースへの接続設定
# db = SqliteDatabase('peewee_db.sqlite')  # SQLite固定の場合
db = connect("sqlite:///peewee_db.sqlite")  # 環境変数に合わせて変更する場合
# db = connect(os.environ.get('DATABASE') or 'sqlite:///peewee_db.sqlite')  # 環境変数が無い場合にデフォルト値として値を設定することも可能

# 接続NGの場合はメッセージを表示
if not db.connect():
    print("接続NG")
    exit()
print("接続OK")


class User(UserMixin, Model):
    # カラムの登録
    id = IntegerField(primary_key=True)  # 数字
    name = CharField()  # 文字
    title = CharField()  # 文字
    body = CharField()  # 文字

    class Mata:
        database = db
        table_name = "users"


db.create_tables([User])


class Massage(UserMixin, Model):
    # カラムの登録
    name = CharField()  # 文字
    title = CharField()  # 文字
    body = CharField()  # 文字

    class Mata:
        database = db
        table_name = "Masssage"


db.create_tables([Massage]) 

id = IntegerField(primary_key=True)  # 数字    


# テーブル
# １．ユーザテーブル
#     社員番号
#     氏名
#     パスワード
# ２，車両テーブル
#     車種
#     オドメーター情報
#     ステータス（空き状況）
