#from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.static import serve

app_name = 'myapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('robots\.txt', lambda r: HttpResponse('User-agent: *\nDisallow: /', content_type='text/plain')),
    path('', TemplateView.as_view(template_name="home.html")),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#if settings.DEBUG:
#  urlpatterns += [
#      re_path(r'^media/(?P<path>.*)$', serve, {
#        'document_root': settings.MEDIA_ROOT, }),
#      ]
