from django.shortcuts import render
from django.template.context_processors import csrf
from load_ssl.forms import LoadCertificate, LoadCertificate_sql
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


def load_ssl(request):

    def data_for_page(form):
        data = {}
        data['form'] = form
        data.update(csrf(request))
        return data

    if request.method == 'POST':
        form = LoadCertificate(
            request.POST,
            request.FILES
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse('view_ssl:all_ssl')
            )
        else:
            return render(
                request,
                'load_ssl.html',
                data_for_page(form)
            )
    else:
        return render(
            request,
            'load_ssl.html',
            data_for_page(LoadCertificate())
        )


def load_ssl_sql(request):

    def data_for_page(form):
        data = {}
        data['form'] = form
        data.update(csrf(request))
        return data

    if request.method == 'POST':
        form = LoadCertificate_sql(
            request.POST,
            request.FILES
        )
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse('view_ssl:all_ssl_sql')
            )
        else:
            return render(
                request,
                'load_ssl.html',
                data_for_page(form)
            )
    else:
        return render(
            request,
            'load_ssl.html',
            data_for_page(LoadCertificate_sql())
        )
