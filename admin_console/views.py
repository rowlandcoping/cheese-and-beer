from django.shortcuts import render

# Create your views here.

def admin_console(request):
    """ Returns admin console page"""
    return render(request, 'admin_console/admin-console.html')
