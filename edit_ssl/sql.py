from ssl_parse.sql import get_connect


def update_cer(id, **kwargs):
    connect = get_connect()
    cursor = connect.cursor()
    set = ''
    for line in kwargs:
        set += '''{0} = '{1}', '''.format(
            line,
            kwargs[line]
        )
    set = set[:-2]
    sql = '''
        UPDATE cert_data
        SET 
            ogrn = NULL,
            inn = NULL,
            snils = NULL,
            ogrnip = NULL,
            organization_name = NULL,
            street_address = NULL,
            locality_name = NULL,
            state_or_province_name = NULL,
            country_name = NULL,
            given_name = NULL,
            surname = NULL,
            common_name = NULL,
            email_address = NULL,
            serial_number = NULL
    '''
    cursor.execute(sql)
    connect.commit()
    sql = '''
        UPDATE cert_data
        SET {0}
        WHERE id = {1};
    '''.format(
        set,
        id
    )
    cursor.execute(sql)
    connect.commit()
    cursor.close()
    connect.close()
