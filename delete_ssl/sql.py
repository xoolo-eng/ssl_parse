from ssl_parse.sql import get_connect
from ssl_parse.settings import MEDIA_ROOT
import os


def del_cert(id):
    connect = get_connect()
    cursor = connect.cursor()
    sql = '''
    SELECT file_certificate
    FROM cert_data
    WHERE id = {0};
    '''.format(id)
    cursor.execute(sql)
    file_name = cursor.fetchone()[0]

    sql = '''
    DELETE FROM cert_data WHERE id = {0};
    '''.format(id)
    cursor.execute(sql)
    connect.commit()
    cursor.close()
    connect.close()
    os.remove(
        '{0}/{1}'.format(
            MEDIA_ROOT,
            file_name
        )
    )
