from django.shortcuts import render
from django.template.context_processors import csrf
from ssl_parse.models import Certificate
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from delete_ssl.sql import del_cert
from view_ssl.sql import get_one_cert


def delete_ssl(request, id):
    '''
        Конечно в идеале необходима проверка что
        пост удаляется и запрс POST и GET совпадают
    '''
    data = {}
    data['cert'] = Certificate.objects.get(id=int(id))
    if request.method == 'POST':
        if request.POST.get('Yes'):
            data['cert'].delete()
            return HttpResponseRedirect(
                reverse('view_ssl:all_ssl')
            )
        else:
            return HttpResponseRedirect(
                reverse('view_ssl:one_ssl', args=(int(id),))
            )
    else:
        data.update(csrf(request))
        return render(request, 'delete_ssl.html', data)


def delete_ssl_sql(request, id):
    data = {}
    data['cert'] = get_one_cert(int(id))
    if request.method == 'POST':
        if request.POST.get('Yes'):
            del_cert(int(id))
            return HttpResponseRedirect(
                reverse('view_ssl:all_ssl_sql')
            )
        else:
            return HttpResponseRedirect(
                reverse('view_ssl:one_ssl_sql', args=(int(id),))
            )
    else:
        data.update(csrf(request))
        return render(request, 'delete_ssl.html', data)
