from django.shortcuts import render, redirect


def reports_index(request):
    return render(request, 'report_page.html', {'nbar': 'reports'})
