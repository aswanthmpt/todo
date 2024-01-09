from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('update/<int:id>',views.Update,name='update'),                                  
    path('delete/<int:id>',views.Delete,name='delete')                                  
]
