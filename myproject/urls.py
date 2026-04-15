"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path
from loginapp import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register_page, name="register"),
    path('login/', views.login_page, name="login"),
    path('', views.home, name='home'),
    path('companies/', views.companies, name='companies'),
    path('postjob/', views.postjob, name='postjob'),
    path('adminlogin/', views.adminlogin_page, name='adminlogin'),
    path('adminregister/',views.adminregister_page,name='adminregister'),
    path('adminhome/',views.admin_home,name='adminhome'),
    path('userdetails/',views.userdetails_page,name='userdetails'),
    # path('userdetailsreview/', views.userdetails_review, name='userdetailsreview'),
    # path('update/<int:id>/', views.update_userdetails, name='updateuserdetails'),
    # path('delete/<int:id>/', views.delete_userdetails, name='deleteuserdetails'),
    path('appliedjobs/', views.applied_jobs, name='appliedjobs'),
    path('applicants/<int:job_id>/', views.applicants, name='applicants'),
    path('browsejob/', views.browsejob_page, name='browsejob'),
    path('profile/', views.profile_review, name='profile'),
    path('userdetailsupdate/<int:id>/', views.userdetails_update, name='userdetailsupdate'),
    path('delete/<int:id>/', views.userdetails_delete, name='delete'),
    path('pro/', views.Profile_page, name='pro'),
    path('update-status/<int:id>/', views.update_status, name='update_status'),
    path('apply/<int:job_id>/', views.apply_job, name='apply_job'),
    path('delete-application/<int:id>/', views.delete_application, name='delete_application'),
    path('update-app-status/<int:id>/<str:status>/', views.update_application_status, name='update_app_status'),  
    path('admindashboard/', views.admin_dashboard, name='admindashboard'),
     path('update/<int:id>/', views.jobupdate, name='update_job'),
    path('delete/<int:id>/', views.delete_job, name='delete_job'),
    path('logout/', views.logout, name='logout'),
    path('close-job/<int:job_id>/', views.close_job, name='close_job'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
