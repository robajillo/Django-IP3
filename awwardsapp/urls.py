from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.home,name='home'),
    path('profile/', views.profile, name='profile'),
    path('new/profile', views.add_profile, name='add_profile'),
    path('search/', views.search_results, name='search_results'),
    path('upload/', views.update_post, name='upload'),
    path('rating/<pk>',views.add_rating,name='rating'),
    path('api/profile/', views.ProfileList.as_view()),
    path('api/post/', views.PostList.as_view()),
    path('api/profile/profile-id',views.ProfileDescription.as_view()),
    path('api/post/post-id',views.PostDescription.as_view())


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
