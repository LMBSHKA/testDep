from django.urls import path
from app import settings
from users import views
from django.conf.urls.static import static

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout, name='logout'),
    path('edit_profile/', views.UserEditView.as_view(), name='edit_profile'),
    path('list/', views.list_images, name='list_images'),
    path('list_achivements/', views.list_images_achivements, name='list_achive'),
    path('list_equipments/', views.equipments, name='list_equipments')
]