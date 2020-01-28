from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from students.views import home_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
    path('students/', include('students.urls')),
    path('teachers/', include('teachers.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
