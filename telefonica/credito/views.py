# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators import csrf
from forms import ClienteForm

# Create your views here.
""" def cliente(request):
	if(request.POST):
		form = ClienteForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/exito/')
	else:
		form = ClienteForm()


	args = {}
	args.update(csrf(request))
	args['form'] = form

	return render_to_response('cliente.html',args)

def exito(request):
	return HttpResponse("Cliente ingresado con Exito")

"""

def cliente(request):
	return render_to_response('cliente.html', {})