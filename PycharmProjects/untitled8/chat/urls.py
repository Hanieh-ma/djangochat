from django.urls import path, re_path

from chat.views import ChatView, MessageListView

urlpatterns = [
    path('message/', ChatView.as_view()),
]
