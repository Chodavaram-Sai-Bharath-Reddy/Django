from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

todos = ['Check emails', 'Takeout trash', 'code']

class AddTodoForm(forms.Form):
    todo = forms.CharField(label="New Task")


def index(request):
    if "todos" not in request.session:
        request.session["todos"] = []
    return render(request, 'todos/index.html', {
        'todos': request.session["todos"]
    })


def add(request):
    if request.method == 'POST':
        form = AddTodoForm(request.POST)
        if form.is_valid():
            todo = form.cleaned_data['todo']
            request.session["todos"] += [todo]
            return HttpResponseRedirect(reverse('todos:index'))
        else:
            return render(request, 'todo/add.html', {
                'form': AddTodoForm(request.POST)
            })
    return render(request, 'todos/add.html', {
        'form': AddTodoForm()
    })
