from ssl_parse.sql import get_connect


def load_cer(**kwargs):
    connect = get_connect()
    cursor = connect.cursor()
    items = '('
    values = '('
    for line in kwargs:
        items += '{0}, '.format(line)
        values += ''''{0}', '''.format(kwargs[line])
    items = items[:-2] + ')'
    values = values[:-2] + ')'
    sql = '''
        INSERT
        INTO
            cert_data
            {0}
        VALUES
           {1};
    '''.format(
        items,
        values
    )
    cursor.execute(sql)
    connect.commit()
    cursor.close()
    connect.close()
