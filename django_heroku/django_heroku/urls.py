# django_heroku > url.py
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    # Home pattern
    path('', TemplateView.as_view(template_name='heroku_app/heroku_app.html')),
    path('admin/', admin.site.urls),
]
