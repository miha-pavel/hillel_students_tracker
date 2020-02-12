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

urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

# https://docs.djangoproject.com/en/3.0/topics/http/views/#customizing-error-views
# https://stackoverflow.com/questions/17662928/django-creating-a-custom-500-404-error-page
# https://medium.com/@MicroPyramid/handling-custom-error-pages-404-500-in-django-ff1f9e0cf2b5
handler404 = 'students.views.handler404'
handler500 = 'students.views.handler500'
