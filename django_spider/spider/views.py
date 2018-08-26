# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

from .models import test_table
from django.http import HttpResponse

def get_age(request):
	name = "wanshuo"
	result = test_table.objects.filter(name="wanshuo").values()
	result = list(result)[0]
	age = result.get("age")
	return HttpResponse("name:" + name + ", age:" + str(age))
