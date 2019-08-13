from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path('list/(?P<userparameter>\d{0,10})', views.conversation_view),
]
