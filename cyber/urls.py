from django.urls import path
from cyber import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
     path("start", views.start),
     path("index", views.index,name="index"),
     path("login", views.loginpage, name = "loginpage"),
     path("signup", views.signuppage, name = "signuppage"),
     path("lets-logout", views.logutnow, name = "logout"),
#      path("login", views.loginpage, name = "loginpage"),
     
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)