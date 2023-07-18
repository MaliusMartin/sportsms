from django.urls import path, include


from . import views

app_name = 'core'
urlpatterns = [
   
    path('', views.index,  name='index'),
    path('sports/', views.sports, name='sports'),
    path('about/', views.about, name='about'),
    path('sports/<int:sport_id>/', views.sport, name='sport'),
    path('categories/', views.index, name='categories'),
    path('details/<int:detail_id>/', views.detail, name='detail'),
    path('search/', views.search, name='search'),

    
     
]