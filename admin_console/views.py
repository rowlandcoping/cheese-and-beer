from django.shortcuts import render, redirect, get_object_or_404
from user_account.models import ContactForm
from checkout.models import Order
from django.contrib import messages
from django.urls import reverse

# Create your views here.

def admin_console(request):
    """ Returns admin console page"""
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'admin_console/admin-console.html')
        return redirect('home')
    else:
        return redirect('home')
    
def view_messages(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            messages = ContactForm.objects.all().order_by('-date')
            template = 'admin_console/view-messages.html',
            context = {
                'user_messages': messages,
            }
            return render(request, template, context)
        return redirect('home')
    else:
        return redirect('home')
    

def order_from_messages(request, order_number):
    if request.user.is_superuser:
        order = get_object_or_404(Order, order_number=order_number)
        return redirect(reverse('order_info', args=[order.id]))
    else:
        return redirect('home')

    
def remove_message(request, message_id):
    if request.user.is_superuser:
        message = get_object_or_404(ContactForm, pk=message_id)
        message.delete()
        messages.success(request, "Message Deleted")
        return redirect('view_messages')
    else:
        return redirect('home')


    
