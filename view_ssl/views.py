from django.shortcuts import render
from django.template.context_processors import csrf
from ssl_parse.models import Certificate
from view_ssl.sql import get_all_cert, get_one_cert


def all_ssl(request):
    '''
        Страница отображения всех сертификатов
    '''
    data = {}
    data['certs'] = Certificate.objects.all().values('name', 'id')
    data.update(csrf(request))
    return render(request, 'view_ssl.html', data)


def one_ssl(request, id):
    '''
        страница отображения одного сертификата
    '''
    data = {}
    data['cert'] = Certificate.objects.get(id=int(id))
    data.update(csrf(request))
    return render(request, 'one_ssl.html', data)


def all_ssl_sql(request):
    data = {}
    data['certs'] = get_all_cert()
    data.update(csrf(request))
    return render(request, 'view_ssl.html', data)


def one_ssl_sql(request, id):
    data = {}
    data['cert'] = get_one_cert(int(id))
    data.update(csrf(request))
    return render(request, 'one_ssl.html', data)
