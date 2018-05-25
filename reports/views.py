from django.shortcuts import render, redirect
from django.template import loader
from production_floor.models import Product
from django.http import HttpResponse
import codecs
import os
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.uploadedfile import SimpleUploadedFile
import pdfkit
import random
import string
import datetime


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def render_to_file(template, filepath, context):
    file = codecs.open(filepath, "w", "utf-8")
    file.write(loader.render_to_string(template, context))
    file.close()


def reports_index(request):
    products = Product.objects.filter(processes='').filter(coc='')
    return render(request, 'report_page.html', {'nbar': 'reports', 'products': products})


def coc(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        if product.coc:
            response = HttpResponse(product.coc, content_type='application/pdf')
            response['Content-Disposition'] = 'filename='+str(product.order.id)+'_'+str(product.id)+'_coc.pdf'
            return response
        else:
            if request.method == 'GET':
                if not product.processes:
                    return render(request, 'coc_form.html', {'nbar': 'reports', 'product': product})
                else:
                    return _not_exist_page(request, 'notFinished')
            else:
                product = Product.objects.get(id=request.POST['product'])
                form = request.POST.copy()
                del form['csrfmiddlewaretoken']
                del form['product']
                data = {
                    'client_name': product.order.clientID.name,
                    'client_address': product.order.clientID.address,
                    'order': product.order.id,
                }
                for field in form:
                    if form[field] != '':
                        data[field] = form[field]
                rand_file = 'reports/templates/utility/' + random_string_generator() + '.html'
                render_to_file('COC.html', rand_file, {"data": data})
                pdf = pdfkit.from_file(rand_file, False, options={'title': 'SHOHAM - C.O.C of part '
                                                                           + str(product.id) + ', order '
                                                                           + str(product.order.id)})
                product.coc = SimpleUploadedFile(str(product.order.id) + '_' + str(product.id) + '_coc.pdf',
                                                 pdf, content_type='application/pdf')
                product.save()
                os.remove(rand_file)
                return redirect('reports:coc', product.id)

    except ObjectDoesNotExist:
        return _not_exist_page(request, 'notExist')


def _not_exist_page(request, error):
        return render(request, 'report_page.html', {'nbar': 'reports',
                                                    'error': error})
