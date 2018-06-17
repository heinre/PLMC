from django.shortcuts import render, redirect
from django.template import loader
from production_floor.models import Product
from orders.models import Order
from clients.models import PotentialClient
from django.http import HttpResponse
import codecs
import os
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.uploadedfile import SimpleUploadedFile
import pdfkit
import random
import string
import json


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def render_to_file(template, filepath, context):
    file = codecs.open(filepath, "w", "utf-8")
    file.write(loader.render_to_string(template, context))
    file.close()


def reports_index(request):
    products = Product.objects.filter(processes='').filter(coc='').filter(coc_needed=True) | \
               Product.objects.filter(processes='').filter(routing='')
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
                    return _not_exist_page(request, 'המוצר לא סיים עיבוד בכל התחנות')
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
                with open('./reports/utilities/globals.json', 'r+') as file:
                    sn = json.load(file)
                    sn['COC'] = sn['COC'] + 1
                    serial = str(sn['COC']).zfill(6)
                    file.seek(0)
                    file.write(json.dumps(sn))
                render_to_file('COC.html', rand_file, {"data": data, 'serial': serial})
                pdf = pdfkit.from_file(rand_file, False, options={'title': 'SHOHAM - C.O.C of part '
                                                                           + str(product.id) + ', order '
                                                                           + str(product.order.id)})
                product.coc = SimpleUploadedFile(str(product.order.id) + '_' + str(product.id) + '_coc.pdf',
                                                 pdf, content_type='application/pdf')
                product.save()
                os.remove(rand_file)
                return redirect('reports:coc', product.id)

    except ObjectDoesNotExist:
        return _not_exist_page(request, 'המוצר אינו קיים')


def delivery(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        if request.method == 'GET':
            if order.doneTime:
                return render(request, 'delivery_form.html', {'nbar': 'reports', 'order': order})
            else:
                return _not_exist_page(request, 'ההזמנה עדיין בתהליכי עיבוד')
        else:
            form = request.POST.copy()
            print(form)
            order = Order.objects.get(id=form['order_number'])
            del form['csrfmiddlewaretoken']
            data = {
                'client_name': order.clientID.name,
                'client_address': order.clientID.address,
            }
            for field in form:
                if form[field] != '':
                    data[field] = form[field]
            rand_file = 'reports/templates/utility/' + random_string_generator() + '.html'
            render_to_file('delivery.html', rand_file, {"data": data})
            pdf = pdfkit.from_file(rand_file, False, options={'title': 'SHOHAM - delivery of order ' + str(order.id)})
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'filename=delivery_' + str(order.id) + '.pdf'
            os.remove(rand_file)
            return response
    except ObjectDoesNotExist:
        return _not_exist_page(request, 'ההזמנה אינה קיימת')


def potential(request, client_id):
    try:
        client = PotentialClient.objects.get(id=client_id)
        rand_file = 'reports/templates/utility/' + random_string_generator() + '.html'
        render_to_file('potential.html', rand_file, {"client": client})
        pdf = pdfkit.from_file(rand_file, False, options={'title': 'SHOHAM - Potential Client ' + client.name})
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'filename=potential_' + str(client.id) + '.pdf'
        os.remove(rand_file)
        return response
    except ObjectDoesNotExist:
        return _not_exist_page(request, 'הלקוח אינו קיים')


def routing(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
        if product.routing:
            response = HttpResponse(product.routing, content_type='application/pdf')
            response['Content-Disposition'] = 'filename='+str(product.order.id)+'_'+str(product.id)+'_routing.pdf'
            return response
        if not product.processes:
            if request.method == 'GET':
                if not product.processes:
                    return render(request, 'routing_form.html', {'nbar': 'reports', 'product': product})
                else:
                    return _not_exist_page(request, 'המוצר לא סיים עיבוד בכל התחנות')
            else:
                product = Product.objects.get(id=request.POST['product'])
                form = request.POST.copy()
                del form['csrfmiddlewaretoken']
                del form['product']
                data = {
                    'product': product,
                    'done_processes': json.loads(product.done_processes),
                }
                for field in form:
                    if form[field] != '':
                        data[field] = form[field]
                rand_file = 'reports/templates/utility/' + random_string_generator() + '.html'
                render_to_file('routing.html', rand_file, {"data": data})
                pdf = pdfkit.from_file(rand_file, False,
                                       options={'title': 'SHOHAM - routing card of product ' + str(product.id)})
                product.routing = SimpleUploadedFile(str(product.order.id) + '_' + str(product.id) + '_routing.pdf',
                                                     pdf, content_type='application/pdf')
                product.save()
                os.remove(rand_file)
            return redirect('reports:routing', product.id)
        else:
            product = Product.objects.get(id=product_id)
            data = {
                'product': product,
                'done_processes': json.loads(product.done_processes),
                'draft': True,
            }
            rand_file = 'reports/templates/utility/' + random_string_generator() + '.html'
            render_to_file('routing.html', rand_file, {"data": data})
            pdf = pdfkit.from_file(rand_file, False,
                                   options={'title': 'SHOHAM - routing card of product ' + str(product.id)})
            os.remove(rand_file)
            return HttpResponse(pdf, content_type='application/pdf')
    except ObjectDoesNotExist:
        return _not_exist_page(request, 'המוצר אינו קיים')


def _not_exist_page(request, error):
        return render(request, 'report_page.html', {'nbar': 'reports',
                                                    'error': error})


def delete_coc(request):
    if request.method == 'GET':
        return _not_exist_page(request, 'הטופס אינו קיים')
    else:
        try:
            product = Product.objects.get(id=request.POST['id'])
            filename = str(product.order.id) + '_' + str(product.id) + '_coc.pdf'
            os.remove('media/coc/'+filename)
            product.coc = ''
            product.save()
            return JsonResponse({'status': 'success', 'order': product.order.id})
        except:
            return JsonResponse({'status': 'fail'})


def delete_routing(request):
    if request.method == 'GET':
        return _not_exist_page(request, 'הטופס אינו קיים')
    else:
        try:
            product = Product.objects.get(id=request.POST['id'])
            filename = str(product.order.id) + '_' + str(product.id) + '_routing.pdf'
            os.remove('media/routing/'+filename)
            product.routing = ''
            product.save()
            return JsonResponse({'status': 'success', 'order': product.order.id})
        except:
            return JsonResponse({'status': 'fail'})
