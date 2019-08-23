from django.urls import path, re_path, include

# from . import views
from . import views

urlpatterns = [
    # path('list/', views.user_list_view),
    path('item/', views.UserListItemView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('signup/', views.SignupView.as_view())
    # path('', include('django.contrib.auth.urls')), # new
]
