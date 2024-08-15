
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sonar/', include('django_sonar.urls')),
    path('', include('core.urls')),
]
