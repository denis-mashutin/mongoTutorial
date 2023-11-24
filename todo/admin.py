from django.contrib import admin

from todo.models import ToDoItem


# Register your models here.
@admin.register(ToDoItem)
class ToDoItemAdmin(admin.ModelAdmin):
    pass
