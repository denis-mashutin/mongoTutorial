from datetime import date, timedelta

from django.test import TestCase
from django.urls import reverse
from .models import ToDoItem


def create_todo(todo_text, days):
    return ToDoItem.objects.create(text=todo_text, due_date=date.today() + timedelta(days=days))


class AllToDosViewTest(TestCase):

    def test_today(self):
        todo = create_todo("To be done today", 0)
        response = self.client.get(reverse("index"))
        self.assertQuerySetEqual(
            response.context["todoitem_list"],
            [todo]
        )

    def test_last_week(self):
        todo = create_todo("This task is past due", -7)
        response = self.client.get(reverse("index"))
        self.assertQuerySetEqual(
            response.context["todoitem_list"],
            []
        )

    def test_next_week(self):
        todo = create_todo("Still have some time", 7)
        response = self.client.get(reverse("index"))
        self.assertQuerySetEqual(
            response.context["todoitem_list"],
            [todo]
        )