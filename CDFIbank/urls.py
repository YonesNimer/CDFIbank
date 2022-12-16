from django.contrib import admin
from django.urls import include, path
from django.shortcuts import redirect
urlpatterns = [
    path('', lambda r: redirect('members/login_user')),
    path('members/', include('members.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]