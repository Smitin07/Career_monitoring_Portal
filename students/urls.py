from django.contrib import admin
from django.urls import path
from students import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('students/', views.students_list),
    path('profile/<int:id>/', views.profile),
    path('add/', views.add_student),
    path('top/', views.top_students),
    path('shortlist/', views.shortlisted_students),
    path('filter/', views.filter_students),
    path('companies/', views.companies),
    path('company/<int:id>/', views.company_detail),
]