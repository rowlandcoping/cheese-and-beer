from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from django.views.decorators.http import require_POST


def account_overview(request):
    redirect('home')


def view_orders(request):
    redirect('home')