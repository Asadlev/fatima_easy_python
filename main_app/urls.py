
from django.urls import path
from  . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'main_app'


urlpatterns = [
    path('', views.main, name='main'),
    path('detail/<int:pk>', views.MethodDetailView.as_view(), name='detail'),
    path('about', views.about,name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
