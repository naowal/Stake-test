from django.shortcuts import render
from .models import Message
from django.utils import timezone

def post_list(request):

    allmsg = Message.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    msglist = list()

    # if press pop button
    if 'popmid' in request.GET and request.GET['popmid']:
        q = request.GET['popmid']
        popMessage = Message.objects.get(mid=q)
        popMessage.delete()

    # if press push button
    elif 'pushmessage' in request.GET and request.GET['pushmessage']:
        q = request.GET['pushmessage']
        pushMessage = Message.objects.create(text=q)
        pushMessage.save()

    # if press startat button
    elif ('startat' in request.GET) and ('startat_msg' in request.GET) and (request.GET['startat']) and (request.GET['startat_msg']):
        startat = int(request.GET['startat'])
        startatmsg = request.GET['startat_msg']
        count = 1
        for msg in allmsg :
            msglist.append(msg)
        msglist.insert(startat-1,startatmsg)   
        # delete all and recreate 
        Message.objects.all().delete()
        # Recreate with msglist
        for msgl in msglist :
            addMsgToDB = Message.objects.create(text=msgl)
        addMsgToDB.save()

    allmsg = Message.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    textlist = list()
    for post in allmsg :
        textlist.append(post)
    if(allmsg): 
        return render(request, 'stakeapp/message_list.html', {'posts': reversed(allmsg) ,'popmessage': textlist[-1]})
    else:
        return render(request,'stakeapp/message_list.html')



