from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    re_path(r'^ajax/nfatodfa/$', views.nfa_to_dfa),
    re_path(r'^contact/$',views.contact,name='contact')
]