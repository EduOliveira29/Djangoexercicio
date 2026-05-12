from django.urls import path

from blog import view
from blog.views import async_view
from blog.views import sync_view

urlpatterns = [
    path('', view.PostView.as_view(), name='home'),
    path('post/<slug:slug>/', view.PostDetail.as_view(), name='post_detail'),
    path('async/', async_view, name='async'),
     path('sync/', sync_view, name='sync'),
]