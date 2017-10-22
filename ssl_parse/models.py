'''
    Модель для хранения данных сертификата, хранит основные
    поля субъекта и сам файл сертефиката
'''
from django.db import models
from asn1crypto import x509
from ssl_parse.settings import MEDIA_ROOT
import subprocess
from datetime import datetime
import os


class Certificate(models.Model):

    def file_load(self, filename):
        date_load = str(datetime.now())
        date_load = date_load.replace(
            '-', '_'
        ).replace(
            ' ', '_'
        ).replace(
            ':', '_'
        ).replace(
            '.', '_'
        )
        filename = filename.replace(
            '-', '_'
        ).replace(
            ' ', '_'
        ).replace(
            ':', '_'
        )
        file = 'certs/{0}_{1}'.format(
            date_load,
            filename
        )
        return file

    name = models.CharField(
        max_length=40,
        verbose_name='Название сертификата'
    )
    ogrn = models.TextField(
        null=True,
        verbose_name='ОГРН'
    )
    inn = models.TextField(
        null=True,
        verbose_name='ИНН'
    )
    snils = models.TextField(
        null=True,
        verbose_name='СНИЛС'
    )
    ogrnip = models.TextField(
        null=True,
        verbose_name='ОГРНИП'
    )
    organization_name = models.TextField(
        null=True,
        verbose_name='Организация'
    )
    street_address = models.TextField(
        null=True,
        verbose_name='Адрес'
    )
    locality_name = models.TextField(
        null=True,
        verbose_name='Местоположение'
    )
    state_or_province_name = models.TextField(
        null=True,
        verbose_name='Регион'
    )
    country_name = models.TextField(
        null=True,
        verbose_name='Страна'
    )
    given_name = models.TextField(
        null=True,
        verbose_name='Имя, Отчество'
    )
    surname = models.TextField(
        null=True,
        verbose_name='Фамилия'
    )
    common_name = models.TextField(
        null=True,
        verbose_name='Название'
    )
    email_address = models.TextField(
        null=True,
        verbose_name='Электронный адрес'
    )
    serial_number = models.TextField(
        null=True,
        verbose_name='Серийный номер'
    )
    file_certificate = models.FileField(
        upload_to=file_load,
        verbose_name='Файл сертификата'
    )

    class Meta:
        db_table = 'cert_data'
        verbose_name = 'Сертификат'
        verbose_name_plural = 'Сертификаты'

    def save(self):
        '''
            При сохранени и парсинге сертификата происходит проверка.
            Если файл не бинарный (pem), то, для удобства и избежания
            проблем с кодировкой, перобразуется в бинарный формат (der)
            и удаляется после парсинга.
        '''
        super(Certificate, self).save()
        file = open(
            '{0}/{1}'.format(MEDIA_ROOT, self.file_certificate),
            'rb'
        )
        data_cert = file.read()
        file.seek(0)
        data = ''
        for line in file:
            try:
                line = line.decode('utf-8')
            except Exception:
                pass
            else:
                data += line
        file.close()
        if len(data):
            cmd = 'openssl x509 -outform der -in "{0}/{1}" -out "{0}/{1}.der"'.format(
                MEDIA_ROOT,
                self.file_certificate,
            )
            proc = subprocess.Popen(
                cmd,
                shell=True
            )
            proc.wait()
            file = open('{0}/{1}.der'.format(
                MEDIA_ROOT,
                self.file_certificate
            ), 'rb')
            data_cert = file.read()
            file.close()
            os.remove('{0}/{1}.der'.format(
                MEDIA_ROOT,
                self.file_certificate
            ))
        cert = x509.Certificate.load(data_cert)
        self.ogrn = cert.subject.native.get('1.2.643.100.1')
        self.inn = cert.subject.native.get('1.2.643.3.131.1.1')
        self.snils = cert.subject.native.get('1.2.643.100.3')
        self.ogrnip = cert.subject.native.get('1.2.643.100.5')
        self.organization_name = cert.subject.native.get('organization_name')
        self.street_address = cert.subject.native.get('street_address')
        self.locality_name = cert.subject.native.get('locality_name')
        self.state_or_province_name = cert.subject.native.get('state_or_province_name')
        self.country_name = cert.subject.native.get('country_name')
        self.given_name = cert.subject.native.get('given_name')
        self.surname = cert.subject.native.get('surname')
        self.common_name = cert.subject.native.get('common_name')
        self.email_address = cert.subject.native.get('email_address')
        self.serial_number = cert.subject.native.get('serial_number')
        super(Certificate, self).save()

    def delete(self):
        os.remove(
            '{0}/{1}'.format(
                MEDIA_ROOT,
                self.file_certificate
            )
        )
        super(Certificate, self).delete()
