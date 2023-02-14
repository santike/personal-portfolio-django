#todas las paginas para el blog
from django.urls import path
#from django.views import render_post
from .views import render_posts, post_detail

app_name = 'blog'

urlpatterns = [
    path('',render_posts, name='posts'),
    path('<int:post_id>', post_detail,name='post_detail'), #para mostrar distintos posts desde vista especial
]