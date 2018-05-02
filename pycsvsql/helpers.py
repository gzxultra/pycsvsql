import datetime
import pandas as pd
from peewee import Model, DateTimeField, CharField, SqliteDatabase

db = SqliteDatabase('pycsvsql.db')

class BaseModel(Model):
    class Meta:
        database = db

    created_time= DateTimeField(default=datetime.datetime.now)
    update_time = DateTimeField(default=datetime.datetime.now)


def read_csv(filename):
    df = pd.read_csv(filename)
    for col_name in df.columns:
        field = CharField(null=False, default='')
        BaseModel._meta.add_field(col_name, field)
        BaseModel._meta.table_name = filename
    return BaseModel
