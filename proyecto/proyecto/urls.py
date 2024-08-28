from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('apl.urls')),
    path('admin/', admin.site.urls),
]
