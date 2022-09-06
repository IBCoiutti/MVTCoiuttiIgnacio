from ast import Return
from contextvars import Context
from http.client import HTTPResponse
from json import load
from multiprocessing import context
from django.shortcuts import render
from .models import Familia
from django.http import HttpResponse
from django.template import loader, context



# Create your views here.

def familia(request):
    familia = Familia(nombre="Jose", apellido="Coiutti", edad=65, parentesco="padre", nacimiento="1956-1-21")
    familia1 = Familia(nombre="Maria", apellido="Miranda", edad=64, parentesco="Madre", nacimiento="1957-1-6")
    familia2 = Familia(nombre="Estefania", apellido="Coiutti", edad=38, parentesco="Hermana", nacimiento="1985-11-13")
    familia3 = Familia(nombre="Simon", apellido="Coiutti", edad=40, parentesco="Hermano", nacimiento="1983-8-21")
    familia.save()
    familia1.save()
    familia2.save()
    familia3.save()
    diccionario = {"nombre":familia.nombre, "apellido":familia.apellido, "edad":familia.edad, "parentesco":familia.parentesco, "nacimiento": familia.nacimiento}
    diccionario1 = {"nombre":familia1.nombre, "apellido":familia1.apellido, "edad":familia1.edad, "parentesco":familia1.parentesco, "nacimiento": familia1.nacimiento}
    diccionario2 = {"nombre":familia2.nombre, "apellido":familia2.apellido, "edad":familia2.edad, "parentesco":familia2.parentesco, "nacimiento": familia2.nacimiento}
    diccionario3 = {"nombre":familia3.nombre, "apellido":familia3.apellido, "edad":familia3.edad, "parentesco":familia3.parentesco, "nacimiento": familia3.nacimiento}
    return render(request, 'template1.html', context={"dic":diccionario,"dic1":diccionario1 , "dic2":diccionario2, "dic3":diccionario3})

