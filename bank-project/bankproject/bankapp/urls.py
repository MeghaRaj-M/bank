from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('kozhikode/', views.kozhikode, name="kozhikode"),
    path('kannur/', views.kannur, name="kannur"),
    path('alappuzha/', views.alappuzha, name="alappuzha"),
    path('trivandrum/', views.trivandrum, name="trivandrum"),
    path('trissur/', views.trissur, name="trissur"),
    path('add_account/', views.add_account, name='add_account'),
    path('get_branches/', views.get_branches, name='get_branches'),
    path('logout', views.logout, name='logout')

]
