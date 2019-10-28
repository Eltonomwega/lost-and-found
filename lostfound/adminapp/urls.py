from django.urls import path
from django.conf.urls import url
from .views import ClaimListView
from . import views

urlpatterns = [
    path('claims', ClaimListView.as_view(), name='claims'),
    url(r'^claims/$', views.claim_search, name='claims_search'),
    url(r'^adminposts/$',views.adminposts_search,name='adminposts_search'),
]