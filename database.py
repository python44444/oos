import datetime
import os
from playhouse.db_url import connect
from dotenv import load_dotenv
from peewee import Model, IntegerField, CharField, TextField, TimestampField

load_dotenv()

db = connect(os.environ.get("DATABASE"))

# 接続NGの場合はメッセージを表示
if not db.connect():
    print("接続NG")
    exit()
print("接続OK")


class User(Model):
    """User Model"""

    id = IntegerField(primary_key=True)  # idは自動で追加されるが明示
    name = CharField()
    title = CharField()
    body = CharField()

    class Meta:
        database = db
        table_name = "users"


db.create_tables([User])


class Cars(Model):
    """Cars Model"""

    id = IntegerField(primary_key=True)  # idは自動で追加されるが明示
    name = CharField()
    title = CharField()
    body = CharField()

    class Meta:
        database = db
        table_name = "cars"


db.create_tables([Cars])


# テーブル (↓ここ本物に書き直し)
# １．ユーザテーブル
#     社員番号
#     氏名
#     パスワード
# ２，車両テーブル
#     車種
#     オドメーター情報
#     ステータス（空き状況）
