from django.contrib import admin
from django.urls import path

from django.views.generic import RedirectView


from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.index),
    # outra forma de redirect
    path('', RedirectView.as_view(url='/agenda/')),
    path('agenda/', views.lista_eventos)
]
