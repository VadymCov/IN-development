from django.urls import path
from accounts import views
from django.contrib.auth import views as auth_views
app_name = "accounts"


urlpatterns = [
    path('registry/', views.RegisterView.as_view(), name='registry'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login' ),
    path('profile/', views.profile, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(template_name='pages/home_page.html', http_method_names=['get', 'post']), name='logout'),
    path('edit_profile/', views.ProfileEditView.as_view(), name='edit_profile'),
] 

