import json
import peewee
from . import field_types
from . import database


def json_parsing(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)


def create_model(table_definition):
    models = []

    for table in table_definition['tables']:
        attrs = {}

        for column in table['columns']:
            field_type = column['type'].split('(')[0]
            field_class = field_types.field_types[field_type]
            attrs[column['name']] = field_class()

            if column.get('primary_key'):
                attrs[column['name']].primary_key = True

            if column.get('foreign_key'):
                foreign_table = column['foreign_key']['table']
                for model in models:
                    if model.__name__ == foreign_table:
                        attrs[column['name']] = peewee.ForeignKeyField(model)
                        break

        DynamicModel = type(table['name'], (peewee.Model,), attrs)
        DynamicModel._meta.database = database.db
        DynamicModel._meta.table_name = table['name']
        models.append(DynamicModel)

    return models
