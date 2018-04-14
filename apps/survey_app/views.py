# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    # response = 'Index'
    return render(request, 'survey_app/index.html')

def processing(request):
    if request.method == 'POST':
        print '*'*50
        # print request.POST
        print request.POST['name']
        # print request.POST['location']
        # print request.POST['language']
        # print request.POST['comment']
        # request.session['name'] = 'test'
        # print request.session['name']
        request.session['name'] = request.POST['name']
        print request.session['name']
        if request.session['name'] == '':
            # flash('Please enter a name')
            return redirect('/')
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        if request.session['comment'] == '':
            # flash('Please enter a comment, up to 120 characters')
            return redirect('/')
        elif len(request.session['comment']) > 120:
        # flash('Please enter a comment, not to exceed 120 characters')
            return redirect('/')
        print '*'*50
        # results = request.session['name'], request.session['location'], request.session['language'], request.session['comment']
    return redirect('/results', name=request.session['name'])
    # else:
    # results = name, location, language, comments
    # return redirect('/')

def results(request):
    return render(request, 'survey_app/results.html')
