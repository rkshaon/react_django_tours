from django.urls import path
from . import views

urlpatterns = [
	path('tour-list/', views.tourList, name="tour-list"),
]
