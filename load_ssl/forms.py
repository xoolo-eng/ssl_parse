from django import forms
from ssl_parse.models import Certificate
from asn1crypto import x509
from load_ssl.sql import load_cer
from ssl_parse.settings import MEDIA_ROOT
from datetime import datetime
import os
from ssl_parse.sql import all_fields
import subprocess


class LoadCertificate(forms.ModelForm):

    class Meta:
        model = Certificate
        fields = ['name', 'file_certificate']

    """
    def clear(self):
        '''
            проверки
        '''
        return self.cleaned_data
    """


class LoadCertificate_sql(forms.Form):
    name = forms.CharField(
        max_length=40,
        label='Название сертификата'
    )
    file_certificate = forms.FileField(
        label='Файл сертификата'
    )

    def save(self):
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

        file_name = str(
            self.cleaned_data.get('file_certificate')
        ).replace(
            '-', '_'
        ).replace(
            ' ', '_'
        ).replace(
            ':', '_'
        )
        if not os.path.exists('{0}/certs/'.format(MEDIA_ROOT)):
            os.mkdir('{0}/certs/'.format(MEDIA_ROOT), mode=0o777)
        new_file = open(
            '{0}/certs/{1}_{2}'.format(
                MEDIA_ROOT,
                date_load,
                file_name
            ),
            'wb'
        )
        new_file.write(self.cleaned_data.get('file_certificate').read())
        new_file.close()
        file = open(
            '{0}/certs/{1}_{2}'.format(
                MEDIA_ROOT,
                date_load,
                file_name
            ),
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
            cmd = 'openssl x509 -outform der -in "{0}/certs/{1}_{2}" -out "{0}/certs/{1}_{2}.der"'.format(
                MEDIA_ROOT,
                date_load,
                file_name
            )
            proc = subprocess.Popen(
                cmd,
                shell=True
            )
            proc.wait()
            file = open('{0}/certs/{1}_{2}.der'.format(
                MEDIA_ROOT,
                date_load,
                file_name
            ), 'rb')
            data_cert = file.read()
            file.close()
            os.remove('{0}/certs/{1}_{2}.der'.format(
                MEDIA_ROOT,
                date_load,
                file_name
            ))
        cert = x509.Certificate.load(data_cert)
        data_cert = {}
        data_cert['name'] = self.cleaned_data.get('name')
        data_cert['file_certificate'] = 'certs/{0}_{1}'.format(date_load, file_name)
        for line in cert.subject.native:
            item = ''
            if line == '1.2.643.100.1':
                item = 'ogrn'
            elif line == '1.2.643.3.131.1.1':
                item = 'inn'
            elif line == '1.2.643.100.3':
                item = 'snils'
            elif line == '1.2.643.100.5':
                item = 'ogrnip'
            else:
                item = line
            if item in all_fields:
                data_cert[item] = cert.subject.native.get(line)
        load_cer(**data_cert)
