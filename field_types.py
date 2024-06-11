import peewee

field_types = {
    'integer': peewee.IntegerField,
    'varchar': peewee.CharField,
    'text': peewee.TextField,
    'timestamp': peewee.TimestampField
}