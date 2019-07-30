"""coaching URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include
from rest_framework import routers
from core.note_api import NoteViewSet
from hotel.hotel_api import AssetViewSet, WorkerViewSet, TaskViewSet, AllocateTaskViewSet
from hotel import views as hotel_views


router  =routers.DefaultRouter()
router.register(r'notes', NoteViewSet)
router.register(r'add-asset', AssetViewSet)
router.register(r'add-task', TaskViewSet)
router.register(r'add-worker', WorkerViewSet)
router.register(r'allocate-task', AllocateTaskViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'', include('core.urls')),
    url(r'api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    url(r'api/', include(router.urls)),
    url(r'api/get-worker-task/(?P<worker_id>\d+)/', hotel_views.GetTask.as_view())
]
