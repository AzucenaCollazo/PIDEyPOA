from django.urls import path
from . import views
# Mandar llamar la vista que imprime el texto bienvenido
urlpatterns = [
    path('', views.login, name='login'),
    path ('index', views.index, name='index'),
    path ('indicadores', views.indicadoress, name='indicadores'),
    path ('indicadores/crear', views.crear_indicador, name='crearindicador'),
    path ('indicadores/editar', views.editar_indicador, name='editarindicador'),
    path('eliminar/<int:id>', views.eliminar_indicador, name='eliminarindicador'),
    path('indicadores/editar/<int:id>', views.editar_indicador, name='editarindicador'),
    path ('estrategias', views.estrategiass, name='estrategias'),
    path ('estrategias/crear', views.crear_estrategia, name='crearestrategia'),
    path ('estrategias/editar', views.editar_estrategia, name='editarestrategia'),
    path('estrategias/eliminar/<int:id>', views.eliminar_estrategia, name='eliminarestrategia'),
    path('estrategias/editar/<int:id>', views.editar_estrategia, name='editarestrategia'),
    path ('areas', views.areass, name='areas'),
    path ('areas/crear', views.crear_area, name='crearareas'),
    path ('areas/editar', views.editar_area, name='editararea'),
    path('areas/eliminar/<int:id>', views.eliminar_area, name='eliminararea'),
    path('areas/editar/<int:id>', views.editar_area, name='editararea'),
    path ('programas', views.programass, name='programas'),
    path ('programas/crear', views.crear_programa, name='crearprograma'),
    path ('programas/editar', views.editar_programa, name='editarprograma'),
    path('programas/eliminar/<int:id>', views.eliminar_programa, name='eliminarprograma'),
    path('programas/editar/<int:id>', views.editar_programa, name='editarprograma'),
    
]