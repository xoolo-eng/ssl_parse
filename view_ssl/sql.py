'''
    Получение всех записей из базы.
    Получение одной записи из базы.
'''
from ssl_parse.sql import get_connect


class MultiData(ValueError):

    def __init__(self, error_message):
        print(error_message)


class NotData(ValueError):

    def __init__(self, error_message):
        print(error_message)


def get_all_cert():
    connect = get_connect()
    cursor = connect.cursor()
    sql = '''
            SELECT
                name,
                ogrn,
                inn,
                snils,
                ogrnip,
                organization_name,
                street_address,
                locality_name,
                state_or_province_name,
                country_name,
                given_name,
                surname,
                common_name,
                email_address,
                serial_number,
                file_certificate,
                id
            FROM cert_data;
        '''
    data = cursor.execute(sql)
    result = []
    for line in data:
        result.append({
            'name': line[0],
            'ogrn': line[1],
            'inn': line[2],
            'snils': line[3],
            'ogrnip': line[4],
            'organization_name': line[5],
            'street_address': line[6],
            'locality_name': line[7],
            'state_or_province_name': line[8],
            'country_name': line[9],
            'given_name': line[10],
            'surname': line[11],
            'common_name': line[12],
            'email_address': line[13],
            'serial_number': line[14],
            'file_certificate': line[15],
            'id': line[16]
        })
    cursor.close()
    connect.close()
    return result


def get_one_cert(id):
    connect = get_connect()
    cursor = connect.cursor()
    sql = '''
            SELECT
                name,
                ogrn,
                inn,
                snils,
                ogrnip,
                organization_name,
                street_address,
                locality_name,
                state_or_province_name,
                country_name,
                given_name,
                surname,
                common_name,
                email_address,
                serial_number,
                file_certificate,
                id
            FROM cert_data
            WHERE id = {0};
        '''.format(id)
    data = cursor.execute(sql)
    result = []
    for line in data:
        result.append({
            'name': line[0],
            'ogrn': line[1],
            'inn': line[2],
            'snils': line[3],
            'ogrnip': line[4],
            'organization_name': line[5],
            'street_address': line[6],
            'locality_name': line[7],
            'state_or_province_name': line[8],
            'country_name': line[9],
            'given_name': line[10],
            'surname': line[11],
            'common_name': line[12],
            'email_address': line[13],
            'serial_number': line[14],
            'file_certificate': line[15],
            'id': line[16]
        })
    cursor.close()
    connect.close()
    if len(result) > 1:
        raise MultiData(
            'Найдено более одного значения'
        )
    elif len(result) == 0:
        raise NotData(
            'Не найдено значений'
        )
    else:
        return result[0]


if __name__ == '__main__':
    data = get_all_cert()
    for line in data:
        print(line)
    data = get_one_cert(3)
    print(data)
