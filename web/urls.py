from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='web-home'),
    path('about/', views.about, name='web-about'),
    path('create/', views.create_post, name='web-create'),
    path('pay/<id>', views.Activity.as_view(), name='web-activity'),

]
