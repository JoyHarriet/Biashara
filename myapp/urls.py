
from django.contrib import admin
from django.urls import path
from myapp import views# from . imoprt views(means current folder)

urlpatterns = [
    path('admin/', admin.site.urls),#leave blank home/
    path('error/', views.error, name='error'),
    path('details/', views.details, name='details'),
    path('blog/', views.blog, name='blog'),
    path('', views.home, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('service/', views.service, name='service'),
    path('starter/', views.starter, name='starter'),
    path('show/', views.show, name='show'),
    

]
