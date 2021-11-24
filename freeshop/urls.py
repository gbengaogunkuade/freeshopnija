"""freeshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from visitor import views as visitor_views
# from market import views as market_views
from market.views import MarketListView
from market import views





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MarketListView.as_view(), name='home'),
    path('about/', visitor_views.about, name='about'),
    path('contact/', visitor_views.contact, name='contact'),
    path('freeshop_register/', visitor_views.freeshop_register, name='freeshop_register'),
    path('freeshop_login/', visitor_views.freeshop_login, name='freeshop_login'),
    path('freeshop_login_to_continue/', visitor_views.freeshop_login_to_continue, name='freeshop_login_to_continue'),
    path('freeshop_logout/', visitor_views.freeshop_logout, name='freeshop_logout'),
    path('freeshop_profile/', visitor_views.freeshop_profile, name='freeshop_profile'),
    path('freeshop_password_change/', visitor_views.freeshop_password_change, name='freeshop_password_change'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='visitor/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='visitor/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='visitor/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='visitor/password_reset_complete.html'), name='password_reset_complete'),
    path('market/', include('market.urls')),
    path('<str:username>/', views.MarketSellerListView.as_view(), name='market_user_post'),
]



if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


