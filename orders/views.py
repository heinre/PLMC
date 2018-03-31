from django.shortcuts import render, redirect


def orders_index(request):
    return render(request, 'order_page.html')
