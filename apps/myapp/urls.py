from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create_pet', views.create_pet),
    path('success', views.success),
    path('<name>', views.name),

]
