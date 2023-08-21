from django.urls import path
from . import views
#login_page
urlpatterns = [
    path('', views.create_user, name='create_user'),
]
