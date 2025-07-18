from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # ✅ Add this
from django.conf.urls.static import static

urlpatterns = [
    path('', include('main.urls')), 
    path('admin/', admin.site.urls),
    path('payments/', include('payments.urls')),
    # other apps...
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)






