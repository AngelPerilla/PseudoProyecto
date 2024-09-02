from django.contrib import admin
from django.urls import include, path
from apl.views import vista1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apl/', include('apl.urls') ),
]
