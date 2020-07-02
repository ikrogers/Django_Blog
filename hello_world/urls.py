from django.urls import path
from hello_world import views

#Careful with spelling. Python will throw crazy unhelpful exception.
urlpatterns = [
    path('', views.hello_world, name='hello_world'),

]