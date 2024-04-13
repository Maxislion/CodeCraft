from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


from .views import HomePageView, AboutPageView, SongsPageView, BlogPageView, ContactPageView, BlogSinglePageView, ContactFormView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/submit/', ContactFormView.as_view(), name='contact_submit'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('songs/', views.index, name='songs'), 
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('blog-single/', BlogSinglePageView.as_view(), name='blog-single'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('new/', views.new, name='new'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_URL)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)