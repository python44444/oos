import datetime
import os
from playhouse.db_url import connect
from dotenv import load_dotenv
from peewee import Model, IntegerField, CharField, TextField, TimestampField,DateField,FloatField
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

    calendar= IntegerField  # idは自動で追加されるが明示
    start_time = DateField()
    endiing_time = DateField()
    task = CharField()
    car_select = CharField()
    select = CharField()
    ODO = FloatField()
    text = TextField()


    class Meta:
        database = db
        table_name = "cars"


db.create_tables([Cars])
