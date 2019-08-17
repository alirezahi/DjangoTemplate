from django.urls import path
from .views import hello_world, render_html

urlpatterns = [
    path('hello_world/<int:django>',hello_world,name='hello_world'),
    path('render_test',render_html, name="render_test")
]
