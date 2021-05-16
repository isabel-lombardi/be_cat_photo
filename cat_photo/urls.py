"""cat_photo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from account.views import SignupAPIView, LogoutAPIView
from upload.views import UploadAPIView
from history.views import ImageList  # , ImageUserView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),

    path("signup/", SignupAPIView.as_view(), name="signup"),

    # After a request containing {"username": "password": } a token associated with the user is returned
    # IT DOES NOT REGENERATE IT
    path("login/", obtain_auth_token, name="login"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path("upload/", UploadAPIView.as_view(), name="upload"),
    path("history/", ImageList.as_view(), name="history"),
    # path("history2/", ImageUserView.as_view(), name="history2"),

]
# To make the URLs of the images accessible.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
