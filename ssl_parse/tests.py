from django.test import TestCase
from django.core.files import File
from ssl_parse.models import Certificate


class CertificateTest(TestCase):

    def test_load_cert(self):
        file = open('1.der', 'rb')
        data = File(file)
        cert = Certificate(
            file_certificate=data,
            name='Test Certificate'
        )
        cert.save()
        print(cert.id)
