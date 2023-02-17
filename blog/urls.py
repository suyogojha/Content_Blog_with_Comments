from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
   path('', home, name='home'),
   path('<slug:post>/', post_single, name='post_single'),
]
