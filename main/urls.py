from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('upload/', views.anotherUploadFunc, name='index'),
    path('', views.mainPage, name='main'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('contact/', views.contact, name='contact'),
    # path('contact/', views.subscribe, name='contact'),
    # path('manager/', views.managerPage, name='manager-page'),
    path('register/', views.registerPage, name='register'),
    path('writers/', views.writersPage, name='writers'),
    path('heroes/', views.heroesPage, name='heroes'),
    path('news_home/', views.addNews, name='add-post'),
    path('new/', views.newsPage, name='new'),
    # path('news/<int:pk>', views.NewsDetailView.as_view(), name='news-detail'),
    # path('news/<int:pk>/update', views.NewsUpdateView.as_view(), name='news-update'),
    # path('news/<int:id>/delete', views.delete, name='news-delete'),
    path('forupload/', views.uploadVideo, name='video-upload'),
    
    
    
    path('new/<slug:post_slug>', views.show_detail, name='news-detail'),
    path('new/<slug:post_slug>/update', views.update_news, name='news-update'),
    path('new/<slug:post_slug>/delete', views.delete_news, name='news-delete'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)