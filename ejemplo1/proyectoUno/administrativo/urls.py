"""
    Manejo de urls para la aplicación
    administrativo
"""
from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('listado-estudiantes', views.listadoEstudiantes,
            name='listadoEstudiantes'),
    path('listado/estudiantes/dos', views.listadoEstudiantesDos,
            name='listadoEstudiantesDos'),
    path('listado/estudiantes/personalizado', views.listadoEstudiantesTelefono,
            name='listadoEstudiantesTelefono '),
    path('listado/estudiantes/cantidadtelefonos', views.listadoCantidadTelefonos,
            name='listadoCantidadTelefonos '),
 ]
