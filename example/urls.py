from django.conf.urls import url, include
from django.contrib import admin
from edc_base.views.login_view import LoginView
from edc_base.views.logout_view import LogoutView
from edc_lab.admin_site import edc_lab_admin

from .views import HomeView

urlpatterns = [
    url(r'^edc/', include('edc_base.urls', namespace='edc-base')),
    url(r'login', LoginView.as_view(), name='login_url'),
    url(r'logout', LogoutView.as_view(pattern_name='login_url'), name='logout_url'),
    url(r'^edc-lab/', include('edc_lab.urls', namespace='edc-lab')),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/', edc_lab_admin.urls),
    url(r'^', HomeView.as_view(), name='home_url'),
]
