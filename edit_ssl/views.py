from django.shortcuts import render
from django.template.context_processors import csrf
from ssl_parse.models import Certificate
from edit_ssl.forms import EditCertificate, EditCertificate_sql
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from ssl_parse.settings import MEDIA_ROOT
import os
from view_ssl.sql import get_one_cert
from edit_ssl.sql import update_cer


def edit_ssl(request, id):

    def data_for_page(form, cert):
        data = {}
        data['form'] = form
        data['cert'] = cert
        data.update(csrf(request))
        return data

    cert = Certificate.objects.get(id=int(id))
    if request.method == 'POST':
        if request.POST.get('Edit'):
            form = EditCertificate(
                request.POST,
                request.FILES
            )
            if form.is_valid():
                data = form.clean()
                file = str(cert.file_certificate)
                cert.name = data.get('name')
                cert.file_certificate = data.get('file_certificate')
                cert.save()
                os.remove(
                    '{0}/{1}'.format(
                        MEDIA_ROOT,
                        file
                    )
                )
                return HttpResponseRedirect(
                    reverse('view_ssl:one_ssl', args=(int(id),))
                )
            else:
                return render(
                    request,
                    'edit_ssl.html',
                    data_for_page(form, cert)
                )
        else:
            return HttpResponseRedirect(
                reverse('view_ssl:one_ssl', args=(int(id),))
            )
    else:
        return render(
            request,
            'edit_ssl.html',
            data_for_page(EditCertificate(), cert)
        )


def edit_ssl_sql(request, id):
    def data_for_page(form, cert):
        data = {}
        data['form'] = form
        data['cert'] = cert
        data.update(csrf(request))
        return data

    cert = get_one_cert(int(id))
    if request.method == 'POST':
        if request.POST.get('Edit'):
            form = EditCertificate_sql(
                request.POST,
                request.FILES
            )
            if form.is_valid():
                form.update(int(id))
                os.remove(
                    '{0}/{1}'.format(
                        MEDIA_ROOT,
                        cert['file_certificate']
                    )
                )
                return HttpResponseRedirect(
                    reverse('view_ssl:one_ssl_sql', args=(int(id),))
                )
            else:
                return render(
                    request,
                    'edit_ssl.html',
                    data_for_page(form, cert)
                )
        else:
            return HttpResponseRedirect(
                reverse('view_ssl:one_ssl_sql', args=(int(id),))
            )
    else:
        return render(
            request,
            'edit_ssl.html',
            data_for_page(EditCertificate_sql(), cert)
        )
