from . import views
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path(r'ckeditor/', include('ckeditor_uploader.urls')),
]
