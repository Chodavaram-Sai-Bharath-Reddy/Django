from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

todos = ['Check emails', 'Takeout trash', 'code']

class AddTodoForm(forms.Form):
    todo = forms.CharField(label="New Task")


def index(request):
    return render(request, 'todos/index.html', {
        'todos': todos
    })


def add(request):
    if request.method == 'POST':
        form = AddTodoForm(request.POST)
        if form.is_valid():
            todo = form.cleaned_data['todo']
            todos.append(todo)
            return HttpResponseRedirect(reverse('todos:index'))
        else:
            return render(request, 'todo/add.html', {
                'form': AddTodoForm(request.POST)
            })
    return render(request, 'todos/add.html', {
        'form': AddTodoForm()
    })
