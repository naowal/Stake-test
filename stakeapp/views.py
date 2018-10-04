from django.shortcuts import render
from .models import Message
from django.utils import timezone

class Stack:

    def __init__(self):
        posts = Message.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
        self.stack = posts

    def add(self, dataval):
# Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
        
# Use list pop method to remove element
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

def post_list(request):
    posts = Message.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'stakeapp/message_list.html', {'posts': posts})