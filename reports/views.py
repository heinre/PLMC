from django.shortcuts import render, redirect
from django.template import loader
from orders.models import Order
from django.http import HttpResponse
import codecs
import os
from django.core.exceptions import ObjectDoesNotExist
from django.core.files.uploadedfile import SimpleUploadedFile
import pdfkit


def render_to_file(template, filename, context):
    file = codecs.open(filename, "w", "utf-8")
    file.write(loader.render_to_string(template, context))
    file.close()


def reports_index(request):
    orders = Order.objects.filter(coc='').exclude(doneTime=None)
    return render(request, 'report_page.html', {'nbar': 'reports', 'orders': orders})


def coc(request, order_id):
    try:
        order = Order.objects.get(id=order_id)
        if order.coc:
            response = HttpResponse(order.coc, content_type='application/pdf')
            response['Content-Disposition'] = 'filename='+str(order.id)+'_coc.pdf'
            return response
        else:
            if order.doneTime:
                render_to_file('COC.html', 'coc.html', {"order": order})
                pdf = pdfkit.from_file('coc.html', False, options={'title': 'SHOHAM - C.O.C for order '+str(order.id)})
                order.coc = SimpleUploadedFile('coc/'+str(order.id)+'_coc.pdf', pdf, content_type='application/pdf')
                order.save()
                os.remove('coc.html')
                return redirect('orders:info', order.id)
            else:
                return _not_exist_page(request, 'notFinished')
    except ObjectDoesNotExist:
        return _not_exist_page(request, 'notExist')



def _not_exist_page(request,error):
        return render(request, 'report_page.html', {'nbar': 'reports',
                                                    'error': error})
