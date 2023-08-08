from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.models import User 

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.homePage, name='home'),
    path('about-us/', views.aboutUs, name='about'),
    path('file-upload/', views.FileUpload, name="file_upload"),
    path('file-download/', views.FileDownload, name="file_download"),
    path('search-document/', views.FileSearch, name="file_download"),
    path('register/', views.AccountRegister, name="registration"),
    path('login/', views.Login, name="login"),
    path('logout/', views.Logout, name="logout"),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)