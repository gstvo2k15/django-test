from django.contrib import admin
from django.urls import path
from core.views import LaunchPatchJobView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/launch-patch/', LaunchPatchJobView.as_view(), name='launch-patch'),
]
