
from django.contrib import admin
from django.urls import path, include
from todolist_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist', include('todolist_app.urls')),
    path('/contact', views.contact, name='contact'),
    path('/about-us', views.about, name='about'),
]
