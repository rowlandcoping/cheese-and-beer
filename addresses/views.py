from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Addresses
from .forms import AddressForm
from django.views.decorators.http import require_POST


def manage_addresses(request):
    if request.user.is_authenticated:
        addresses= Addresses.objects.filter(user_id=request.user.id).order_by('-default', 'id').values()
        template = 'addresses/addresses.html'    
        context = {
            'addresses': addresses,
        }
        return render(request, template, context)
    else:
        return redirect('account_login')


def add_address(request):
    if request.method=='POST':
        form = AddressForm(request.POST)
        if request.POST.get('origin') == "checkout":
            return_url="checkout"
        else:
            return_url="manage_addresses"
        if form.is_valid():
            final_form = form.save(commit=False)  
            final_form.user_id = request.user
            addresses= Addresses.objects.filter(user_id=request.user.id)
            if addresses:
                if request.POST.get('default'):                
                    for address in addresses:
                        Addresses.objects.filter(pk=address.id).update(
                            default=False
                        )
                    final_form.default = True
            else:
                final_form.default = True
            if request.POST.get('selected'):
                selected_address = {}
                selected_address['postcode'] = form.cleaned_data["postcode"]
                selected_address['address_line_one'] = form.cleaned_data["address_line_one"]
                request.session['selected_address'] = selected_address
            final_form.save()
            messages.success(request, 'Address Added')
        else:
            messages.error(request, 'Sorry, your address was not added, please try again.')
        return redirect(return_url)
    if request.user.is_authenticated:
        template = 'addresses/add-address.html'
        address_form = AddressForm()
        context = {
            'address_form': address_form,
        }
        return render(request, template, context)
    else:
        return redirect('account_login')


def edit_address(request, address_id):
    if request.method=='POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            final_form = form.save(commit=False)
            final_form.user_id = request.user
            final_form.id = address_id
            if request.POST.get('default'):
                addresses= Addresses.objects.filter(user_id=request.user.id)
                for address in addresses:
                    Addresses.objects.filter(pk=address.id).update(
                        default=False
                    )       
                final_form.default = True
            final_form.save()
            messages.success(request, 'Address Updated')
            return redirect('manage_addresses')
        else:
            messages.error(request, 'Sorry, your address was not updated, please try again.')
    if request.user.is_authenticated:
        address = get_object_or_404(Addresses, pk=address_id)
        if request.user == address.user_id:
            template = 'addresses/edit-address.html'
            address_form = AddressForm(instance=address)
            context = {
                'address_form': address_form,
                'address': address,
            }
            return render(request, template, context)
        else:
            return redirect('home')
    else:
        return redirect('account_login')


def remove_address(request, address_id):
    address = get_object_or_404(Addresses, pk=address_id)
    default = address.default
    if request.user == address.user_id:
        address.delete()
        addresses= Addresses.objects.filter(user_id=request.user.id)
        if addresses:
            if default:
                default_default = Addresses.objects.filter(user_id=request.user.id).order_by('id').values()[:1]
                Addresses.objects.filter(pk=default_default[0]['id']).update(
                    default=True
                )
        messages.success(request, 'Address Removed')
        return redirect('manage_addresses')
    else:
        return redirect('home')
    

def set_default(request, address_id):
    address = get_object_or_404(Addresses, pk=address_id)
    if request.user == address.user_id:
        addresses= Addresses.objects.filter(user_id=request.user.id)
        for address in addresses:
            Addresses.objects.filter(pk=address.id).update(
                default=False
            )
        Addresses.objects.filter(pk=address_id).update(
            default=True
        )
        messages.success(request, 'Default Address Changed')
        return redirect('manage_addresses')
    else:
        return redirect('home')
    
    
def use_default(request):
    if 'selected_address' in request.session:
        del request.session['selected_address']
    return redirect('checkout')
    

@require_POST
def select_address(request):
    if 'selected_address' in request.session:
        del request.session['selected_address']
    id = request.POST.get('address_selector')
    address = get_object_or_404(Addresses, pk=id)
    selected_address = {}   
    selected_address['postcode'] = address.postcode
    selected_address['address_line_one'] = address.address_line_one
    request.session['selected_address'] = selected_address
    return redirect('checkout')