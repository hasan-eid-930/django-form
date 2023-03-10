from django.contrib import admin
from django.urls import include, path ,re_path
from django.conf.urls.static import static
from django.views.static import serve
from . import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/', include('app1.urls')),
    # re_path(r'^download/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT})

]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)