#Blog
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('blog_entries/', views.blog_entries, name="blog_entries"),
    path('blog_entries/<int:blog_id>/', views.blog_entry, name="blog_entry")

]