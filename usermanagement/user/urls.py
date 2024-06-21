from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('login/', views.login_page, name='loginpage'),
    path('signup/', views.signup_page, name='signuppage'),
    path('signupsuccess/', views.signup_success, name='signupsuccess'),
    path('userprofile/', views.user_profile, name='userprofile'),
    path('editprofile/', views.edit_profile, name='editprofile'),
    path('logout/', views.logout, name='logout'),

    path('manage_users/', views.admin_manage_users, name='manage_users'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('login_admin/', views.login_admin, name='login_admin'),
    path('logout_admin/', views.logout_admin, name='logout_admin'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
