from django.shortcuts import render

def post_list(request):
    return render(request, 'stakeapp/message_list.html', {})