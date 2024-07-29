from django.urls import path
from vbc import views

urlpatterns = [
    path("estudiante/listar", views.EstudianteListView.as_view(), name = "ListarEstudiantes"),
    path("estudiante/<pk>", views.EstudianteDeleteView.as_view(), name = "EstudiantesBorrar"),
    path("estudiante/<pk>/actualizar", views.EstudianteUpdateView.as_view(), name = "ActualizarEstudiantes"),
]