
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_view
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',user_views.register,name='register'),
    path('profile/',user_views.profile,name='profile'),
    path('login/',auth_view.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('password_reset/',auth_view.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password-reset'),
    # path('password_reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password-reset-done'),
    path('',include('myapp.urls')),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
