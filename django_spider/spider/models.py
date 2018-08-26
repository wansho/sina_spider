# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class test_table(models.Model): # models.Model 代表 该类是 models.Model 的子类
	
	def __str__(self):
		return self.name # 作为该对象的描述
	
	name = models.CharField(max_length=20)
	age = models.IntegerField(default=0)