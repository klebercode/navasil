# coding: utf-8
from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

import json

from crm.core.models import Customer


def list_customers(request):
    customers = Customer.objects.all()
    items = serializers.serialize('json', customers)
    result = json.dumps(items)
    # , content_type="application/json") não precisa no Django 1.7
    return HttpResponse(result, content_type='application/json')
