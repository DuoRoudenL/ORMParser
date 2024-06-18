import database.models
import database.database
import sys


if __name__=='__main__':
    if len(sys.argv) != 2:
        print('Usage: python app.py <file_path>')
        sys.exit()
    file_name = sys.argv[1]
    table_definition = None
    try:
        table_definition = database.models.json_parsing(file_name)
    except Exception as e:
        print(f'Error! {e}')
        sys.exit()
    models = database.models.create_model(table_definition)
    database.database.db.create_tables(models)
