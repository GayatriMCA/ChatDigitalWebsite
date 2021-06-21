from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage,name='register'),
    path('login/',views.loginPage, name='login'),
    path('',views.homePage,name='home'),
    path('logout/',views.logoutUser,name='logout'),
    #path('',views.home,name='home'),
    path('<str:room>/',views.room,name='room'),
    path('checkview',views.checkview,name='checkview'),
    path('send',views.send,name='send'),
    path('getMessages/<str:room>/',views.getMessages,name='getMessages'),
    path('',views.leaveRoom)
]