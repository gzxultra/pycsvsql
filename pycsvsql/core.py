# coding: utf-8
import datetime

import click
from peewee import CharField, DateTimeField, Model, SqliteDatabase
from pycsvsql.helpers import next_n_lines


db = SqliteDatabase('pycsvsql.db')


class BaseModel(Model):
    class Meta:
        database = db

    created_time = DateTimeField(default=datetime.datetime.now)
    update_time = DateTimeField(default=datetime.datetime.now)


def init_database(filename):
    f = open(filename, 'r')
    headers = f.readline()
    fields = []
    for col_name in headers.strip().split(','):
        field = CharField(null=False, default='')
        fields.append(field)
        BaseModel._meta.add_field(col_name, field)
        BaseModel._meta.table_name = filename

    BaseModel.create_table()

    with db.atomic():
        while True:
            lines = next_n_lines(f, 100)
            if not lines:
                break
            data_source = [i.split(',') for i in lines]
            BaseModel.insert_many(data_source, fields=fields).execute()

    f.close()
    return BaseModel


@click.command()
@click.option('--file', default='sample.csv', prompt='name of your csv file')
def pycsvsql(file):
    model_clazz = init_database(file)
    return model_clazz


if __name__ == '__main__':
    pycsvsql()
