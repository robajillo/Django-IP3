from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('', views.home,name='home'),
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/<username>/', views.profile, name='profile'),
    path('profile/<username>/settings', views.edit_profile, name='edit'),
    path('search/', views.search_results, name='search_results'),
    path('upload/', views.update_post, name='upload'),
    path('<username>/profile', views.user_profile, name='userprofile'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rating/<pk>',views.add_rating,name='rating'),
    path('api/profile/', views.ProfileList.as_view()),
    path('api/post/', views.PostList.as_view()),
    path('api-token-auth/', obtain_auth_token),
    path('api/profile/profile-id/',views.ProfileDescription.as_view()),
    path('api/post/post-id/',views.PostDescription.as_view()),
    path('project/<post>', views.project, name='project'),
    path('upload/', views.update_post, name='upload'),

   

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
