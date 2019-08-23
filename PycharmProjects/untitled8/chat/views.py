from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse
from django.utils.datastructures import MultiValueDictKeyError

from chat.celery import app
from chat.models import Messages, Conversations

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from chat.serializers import RequestChatSerializer, ResponseMessageListSerializer
from djangochat.utils import CsrfExemptSessionAuthentication
from rest_framework.authentication import BasicAuthentication 
from django.contrib.auth.models import AnonymousUser



class MessageListView(APIView):

    def get(self, request):
        messages = Messages.objects.all()
        serializer = ResponseMessageListSerializer(
            messages,
            many=True
        )
        return Response(
            {
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )


class ChatView(APIView):

    authentication_classes = (
        CsrfExemptSessionAuthentication, BasicAuthentication)

    def post(self, request):
        if type(request.user) is AnonymousUser:
            return Response({
                'message': 'Unauthorize!!!!'
            }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            serializer = RequestChatSerializer(
                data=request.data,
                context={
                    'user': request.user
                }
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {
                        'message': 'Message saved!'
                    }
                )
            else:
                return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )

@app.task
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# def register(request):
#     if request.user.is_authenticated():
#         return redirect(home)
#     registration_form = RegistrationForm()
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             datas={}
#             datas['username']=form.cleaned_data['username']
#             datas['email']=form.cleaned_data['email']
#             datas['password1'] = form.cleaned_data['password1']
#
#             # We generate a random activation key
#             salt = hashlib.sha1(str(random.random())).hexdigest()[:5]
#             usernamesalt = datas['username']
#             if isinstance(usernamesalt, unicode):
#                 # usernamesalt = usernamesalt.encode('utf8')
#              datas['activation_key'] = hashlib.sha1(salt + usernamesalt).hexdigest()
#
#             datas['email_path'] = "/ActivationEmail.txt"
#             datas['email_subject'] = "Activation de votre compte yourdomain"
#
#             form.sendEmail(datas)
#             form.save(datas)
#             request.session['registered'] = True  # For display purposes
#             return redirect(home)
#         else:
#             registration_form = form  # Display form with error messages (incorrect fields, etc)
#
#     return render(request, 'siteApp/register.html', locals())
