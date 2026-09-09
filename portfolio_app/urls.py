from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('blog/', views.blog_list_view, name='blog_list'),
    path('blog/<slug:slug>/', views.blog_detail_view, name='blog_detail'),
    path('api/contact/', views.contact_api, name='contact_api'),
]
