"""bookmarks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from courses.views import CourseListView

from users import views as user_views
from users import views as blog_views 
from django.contrib.auth import views as auth_views
from django.conf import settings

from acad import views as acad_views
from blogs import views as blogs_views

urlpatterns = [


    path('social-auth/', include('social_django.urls', namespace='social')),
     path('admin/', admin.site.urls),
     path('', include('blog.urls')),
     path('register/', user_views.register,name='register'),
     path('profile/', user_views.profile,name='profile'),
    #  path('login/', auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
     path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
     path('password-reset/', auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
     path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
     path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
     path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
    
     path('login/', user_views.LoginViewUser.as_view(),name='login'),
     path('resources/', acad_views.ResourceListView.as_view(),name='resource_list'),
     path('resources/upload/', acad_views.upload_resource,name='upload_resource'), 
     path('course/', include('courses.urls')),
     path('ac', CourseListView.as_view(), name='course_list'),
     path('students/', include('students.urls')),
     path('blogs/', include('blogs.urls', namespace='blogs')),
    
    # path('free',blogs_views.post_list, name='post_list'),
   
    # path('free/<int:year>/<int:month>/<int:day>/<slug:post>/',
    #      blogs_views.post_detail,
    #      name='post_detail'),
    # path('free/<int:post_id>/share/',
    #      blogs_views.post_share, name='post_share'),
    # path('free/tag/<slug:tag_slug>/',
    #      blogs_views.post_list, name='post_list_by_tag'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
