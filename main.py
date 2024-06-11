import peewee
import json
import database
import field_types


def json_parsing(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)


def create_model(table_definition):

    attrs = {}
    for column in table_definition['columns']:
        field_type = column['type'].split('(')[0]
        field_class = field_types.field_types[field_type]
        attrs[column['name']] = field_class()

    DynamicModel = type(table_definition['table_name'], (peewee.Model,), attrs)
    DynamicModel._meta.database = database.db
    DynamicModel._meta.table_name = table_definition['table_name']

    return DynamicModel


table_definition = json_parsing('table_definition.json')
dynamic_model = create_model(table_definition)
database.db.create_tables([dynamic_model])
