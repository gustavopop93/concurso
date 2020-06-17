from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

urlpatterns += [
    path(r'editar/', views.editarCalendario, name='editar'),
]

urlpatterns += [
    path(r'calendario/<int:pk>/', views.calendario, name='calendario'),
    path('actividad/<int:pk>/', views.detalle_actividad, name='detalle_actividad'),
]