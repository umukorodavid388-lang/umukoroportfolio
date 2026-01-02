from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio-details/<int:pk>', views.portfolio_details, name='portfolio-details'),
    path('services-details/<int:po>', views.services_details, name='services-details'),
    path('services', views.services, name='services'),
    path('testimonal', views.form, name='form'),
    path("download-resume/", views.download_resume, name="download_resume"),
]
