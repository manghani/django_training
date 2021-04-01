from django.urls import path
from . import views

urlpatterns = [
    path('post/<str:name>/<int:age>/<str:add>/<int:marks>', views.save, name = 'save'),
    path('get_all', views.get_all, name = 'get_all'),
    path('get/<str:name>', views.get_data, name = 'get_data'),
    path('delete/<str:name>', views.delete, name = 'delete'),
    path('count', views.count, name = 'count'),
    path('Pass', views.Pass, name = 'Pass')
]
