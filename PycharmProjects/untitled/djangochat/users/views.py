from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from users.models import Users, Messages, Conversations



def conversation_view(request, userparameter):
    if request.method == 'GET':
        pass

    elif request.method == "POST":
        try:
            print(request.POST['message'])
            u = Users.objects.filter(first_name="sara")[0]
            c = Conversations.objects.filter(
                id=int(userparameter))[0]
            Messages(
                sender_id=u,
                conversation_id=c,
                text=request.POST['message'],
                date=datetime.now()
            ).save()
        except ValueError:
            print("there is no userparameters")


    try:
        messages = Messages.objects.filter(
            conversation_id=int(userparameter)
        )
    except ValueError:
        messages =  []

    return render(
        request,
        'userlist.html',
        {
            "messages": messages,
            "conversations": Conversations.objects.all()
        }
    )