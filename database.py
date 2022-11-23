# これデータベースpythonね
<<<<<<<<< Temporary merge branch 1
from playhouse.db_url import connect
from dotenv import load_dotenv
from peewee import Model, IntegerField, CharField, TextField, TimestampField
import datetime
from flask_login import UserMixin

load_dotenv()

db = connect(os.environ.get("DATABASE"))

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


class Message(UserMixin, Model):
    # カラムの登録
    name = CharField()  # 文字
    title = CharField()  # 文字
    body = CharField()  # 文字

    class Mata:
        database = db
        table_name = "Masssage"


db.create_tables([Message])

id = IntegerField(primary_key=True)  # 数字


# テーブル
=========
import os
from playhouse.db_url import connect
from dotenv import load_dotenv
from peewee import Model, IntegerField, CharField, TextField, TimestampField
import datetime

load_dotenv()

db = connect(os.environ.get('DATABASE'))

if not db.connect():
    print("接続NG")
    exit()

# テーブル (↓ここ本物に書き直し)
>>>>>>>>> Temporary merge branch 2
# １．ユーザテーブル
#     社員番号
#     氏名
#     パスワード
# ２，車両テーブル
#     車種
#     オドメーター情報
#     ステータス（空き状況）
