from django.db import models
import ast


class ListFiled(models.Field):
    description = "List Filed"

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 600
        super().__init__(*args, **kwargs)

    def db_type(self, connection):
        return 'text'

    def to_python(self, value):
        if value is None or value == '':
            return []
        elif isinstance(value, str):
            return ast.literal_eval(value)
        else:
            raise TypeError

    def from_db_value(self, value, expression, connection):
        if value is None or value == '':
            return []
        elif isinstance(value, str):
            return ast.literal_eval(value)
        else:
            raise TypeError

    def get_prep_value(self, value):
        if value is None:
            return '[]'
        return str(value)
