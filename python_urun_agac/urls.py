"""python_urun_agac URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from agac import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('qrkod_sele/<int:id>', views.qrkod_sele, name="qrkod_sele"),
    path('qrkod_tekerlek/<int:id>', views.qrkod_tekerlek, name="qrkod_tekerlek"),
    path('qrkod_govde/<int:id>', views.qrkod_govde, name="qrkod_govde"),
    path('qrkod_bisiklet/<int:id>', views.qrkod_bisiklet, name="qrkod_bisiklet"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
