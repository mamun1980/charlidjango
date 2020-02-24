from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_required(TemplateView.as_view(template_name="home.html")), name="home"),
    path('public/', TemplateView.as_view(template_name="public.html"), name="home"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name="login_page.html"), name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/public/'), name="logout"),

    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^pages/', include(wagtail_urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
