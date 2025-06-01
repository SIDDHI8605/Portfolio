from django.urls import path
from . import views
from .views import  thank_you_view  # 👈 Import the view
urlpatterns = [
    path('', views.home,name="home"),
    path('about/', views.about,name="about"),

    path('projects/', views.projects, name="projects"),

    path('certificate/', views.certificate, name="certificate"),

    path('contact/', views.contact, name="contact"),

    path('thank_you/', views.thank_you_view, name="thank_you"),

    path('resume/', views.resume, name="resume"),

    path('success/', views.success, name="success"),

    # urls.py
    # path('thank-you/', thank_you_view, name='contact_thankyou'),
    
]
