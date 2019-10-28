from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from .filters import PostFilter
from . import views
from .views import ClaimCreateView, PostListView

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('claimitem/<int:post_id>/', views.claimitem, name='claimitem'),
    path('postitem', views.postitem, name='postitem'),
    
    path('claim/<object>/', ClaimCreateView.as_view(), name='claim'),
    url(r'^posts/$', views.posts_search, name='posts_search'),
    path('posts', PostListView.as_view(), name='posts'),
]