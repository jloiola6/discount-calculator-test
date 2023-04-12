from django.urls import include, path

from back.apps.core.views import index


app_name = 'core'
 
urlpatterns = [
    path('', index, name='index')
]