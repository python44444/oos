import datetime
import os
from playhouse.db_url import connect
from dotenv import load_dotenv
# from flask import current_user
from peewee import (
    Model,
    IntegerField,
    CharField,
    FloatField,
    TimestampField,
    DateField,
    CharField,
)
from flask_login import UserMixin

# load_dotenv()

db = connect("sqlite:///peewee_db.sqlite")
# db = connect(os.environ.get("DATABASE"))

# 接続NGの場合はメッセージを表示
if not db.connect():
    print("接続NG")
    exit()
print("接続OK")


class User(UserMixin, Model):
    """User Model"""

    id = IntegerField(primary_key=True)  # idは自動で追加されるが明示
    name = CharField()
    password = CharField()
    title = CharField()
    body = CharField()

    class Meta:
        database = db
        table_name = "users"


db.create_tables([User])


class Cars(UserMixin, Model):
    """Cars Model"""

    id = IntegerField(primary_key=True)  # idは自動で追加されるが明示
    use_date = CharField()  # idは自動で追加されるが明示
    start_time = DateField()
    ending_time = DateField()
    task = CharField()
    car_select = CharField()
    member_select = CharField()
    ODO = IntegerField()
    oil = CharField()
    text = CharField()

    class Meta:
        database = db
        table_name = "cars"


db.create_tables([Cars])


class Photos(UserMixin, Model):

    yusou1 = CharField()
    kyuuzyo1 = CharField()
    kagaku1 = CharField()
    tank1 = CharField()
    suisou1 = CharField()
    hashigo1 = CharField()
    shien1 = CharField()
    dankouhou1 = CharField()
    renraku11 = CharField()
    renraku10 = CharField()
    renraku1 = CharField()
    yobisekisai = CharField()
    danshirei1 = CharField()
    danshirei20 = CharField()
    kyuukyuu20 = CharField()
    tank20 = CharField()

    class Meta:
        database = db
        table_name = "photos"


db.create_tables([Photos])
