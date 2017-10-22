from ssl_parse.settings import DATABASES
import pymysql
import sqlite3


def get_connect():
    db = DATABASES['default']
    type_db = db['ENGINE'].split('.')[-1]
    if type_db == 'sqlite3':
        connect = sqlite3.connect(db['NAME'])
    if type_db == 'mysql':
        connect = pymysql.connect(
            host=db['HOST'],
            name=db['NAME'],
            user=db['USER'],
            password=db['PASSWORD'],
            charset=db['CHARSET'] or 'utf8'
        )
    return connect


all_fields = [
    'ogrn',
    'inn',
    'snils',
    'ogrnip',
    'organization_name',
    'street_address',
    'locality_name',
    'state_or_province_name',
    'country_name',
    'given_name',
    'surname',
    'common_name',
    'email_address',
    'serial_number'
]