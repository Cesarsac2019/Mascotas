from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView

urlpatterns = [
    url( r'^login/$',auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    # url(r'^login/$', auth_views.login, name='login'),
    # url(r'^logout/$',auth_views.logout, name='logout'),
]
