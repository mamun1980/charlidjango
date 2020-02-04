from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(TemplateView.as_view(template_name="home.html")), name="home"),
    path('public/', TemplateView.as_view(template_name="public.html"), name="home"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="login_page.html"), name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/public/'), name="logout"),
]
