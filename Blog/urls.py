from django.contrib import admin
from django.urls import path, include
from posting.views import index, DetailPosting, index, AddPost, UpdatePost, SearchPosting
from django.conf import settings
from django.conf.urls.static import static 
from posting import views
from django.contrib.auth import views as auth_views
from posting.views import SearchPosting

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('detail/<int:pk>', views.DetailPosting.as_view(), name='detail'),
    path('add/', views.AddPost.as_view(), name='add'),
    path('<int:pk>/update', views.UpdatePost.as_view(), name='add'),
    path('search/', SearchPosting.as_view(), name='search'),
    path('accounts/', include('allauth.urls')),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

