"""
URL configuration for onewebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.one),
    path('index',views.one),
    path('BLOG',views.three),
      path('from',views.four),
      path('ac',views.five),
      path('suraj',views.web),
      path('register',views.six),
      path('done',views.send),
      path('shop',views.seven),
      path('cart',views.eight),
      path('check',views.pro),
      path('addcart',views.addcart),
      path('delete',views.delete),
      path('forgot',views.ten),
      path('update',views.update),
      path('uptodate',views.uptodata),
      path('forgot',views.forgotpw),
      path('password',views.forgot),





     

     
]   + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
