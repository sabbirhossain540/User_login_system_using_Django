from django.conf.urls import url
from basic_app import views

#TEMPLATE TAGS
app_name = 'basic_app'

urlpatterns=[
    url(r'^register/', views.register,name='register'),
]
