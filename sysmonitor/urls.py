from django.urls import path
from . import views

urlpatterns = [
   path("", views.index, name="index"),
   path("updated_values/", views.updated_values, name='updated_values'),
   path("cpu_view/", views.cpu_view, name="cpu_view"),
   path("ram_view/", views.ram_view, name="ram_view"),
   path("drives_view/", views.drives_view, name="drives_view"),
   path("sys_view/", views.sys_view, name="sys_view")
]