from django.urls import path
from Lewis44.views import *

app_name = 'Lewis44'

urlpatterns = [
    path('' ,index_view,name='index'),
    path('about',about_view,name='about'),
    path('contact',contact_view,name='contact'),
]