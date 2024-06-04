from django.urls import path

from . import views

urlpatterns = [
    path('',views.posts),
    path('create',views.create_post)
]
