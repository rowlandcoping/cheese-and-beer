from django.shortcuts import render, redirect

# Create your views here.

def admin_console(request):
    """ Returns admin console page"""
    if request.user.is_authenticated:
        return render(request, 'admin_console/admin-console.html')
    else:
        return redirect('home')
