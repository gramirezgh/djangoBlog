# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# def lista_post(request):
#     return render(request, "lista_post.html")

# def post_solo(request):
#     return render(request, "post_solo.html")

def contacto(request):
    return render(request, "contacto.html")