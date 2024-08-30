from django.urls import path
from apl.views import *
from apl.views.categoria.views import lista_categoria

app_name = 'apl'
urlpatterns = [
    path('categoria/listar/', lista_categoria, name= 'categoria_lista'),
]