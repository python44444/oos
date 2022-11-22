# これデータベースpythonね
# テーブル
# １．ユーザテーブル
#     社員番号
#     氏名
#     パスワード
# ２，車両テーブル
#     車種
#     オドメーター情報
#     ステータス（空き状況）
from playhouse.db_url import connect
from peewee import Model, IntegerField, CharField
from flask_login import UserMixin

db = connect("sqlite:///peewee_db.sqlite")

if not db.connect():
    print("connection error")
    exit()
print("connection success")

# ここでテーブル作ってねg
