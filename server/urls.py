from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/',include('api.v1.auth.urls')),
    path('api/v1/posts/',include('api.v1.posts.urls'))
]
