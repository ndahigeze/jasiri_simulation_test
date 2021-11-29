from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('', views.login_view, name='login'),
    path('accounts/signup/', views.signup_view, name='signup'),
    path("accounts/logout/",views.logout_view,name="logout")

]