from django.urls import path

from .views import homepage,family ,animal,animal1

urlpatterns = [
    
    path('', homepage),
    path('family/<int:num>', family),
    path('animal/<int:num>', animal, name='animal'),
    path('animal', animal1)
    
]