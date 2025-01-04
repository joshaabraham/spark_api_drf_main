from django.urls import path
from rest_framework import routers
from user_app.api import views

router = routers.SimpleRouter()

urlpatterns = [
    path('register', views.RegisterView.as_view()),
    path('login', views.LoginView.as_view()),
    path('user', views.UserView.as_view()),
    path('logout', views.LogoutView.as_view()),
]
urlpatterns += router.urls
