from django.shortcuts import render
from django.http import HttpResponseRedirect
from todo_app.models import TodoItem

# Create your views here.


def display_todos(request):
    all_items = TodoItem.objects.all()
    return render(request, 'todo.html', {'all_items': all_items})


def add_todo(request):
    new_item = TodoItem(content=request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/todo')


def done_todo(request, todo_id):
    done_item = TodoItem.objects.get(id=todo_id)
    done_item.done = not done_item.done
    done_item.save()
    return HttpResponseRedirect('/todo')


def delete_all(request):
    for item in TodoItem.objects.all():
        item.delete()
    return HttpResponseRedirect('/todo')
