from django.urls import path 
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('account/<name>',views.account,name='account'),
    path('gallery/<id>/<name>',views.gallery,name='gallery'),
    path('adventure/<id>/<name>',views.adventure,name='adventure'),
    path('nature/<id>/<name>',views.nature,name='nature'),
    path('historical/<id>/<name>',views.historical,name='historical'),
    path('about/<name>',views.about,name='about'),
    path('<name>',views.backindex,name='backindex'),
    path('register/',views.registration,name='register'),
    path('hotelanddetails/<destination_id>/<name>/<id>',views.hotelandaboutplace,name='hotelanddetails'),
    path('check/<name>/<hotelname>/<hotelprice>/<id>/<destination_id>/<g_name>',views.check,name='checkroom'),
    path('delete/<name>/',views.delete,name='delete'),
    path('forgectpassword/',views.password,name='password'),

]

