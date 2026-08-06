from django.contrib import admin
from django.urls import path
from students import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home),
    path('add/', views.add_student),
    path('students/', views.students_list),
    path('profile/<int:id>/', views.profile),
    path('top/', views.top_students),
    path('shortlist/', views.shortlisted_students),
    path('filter/', views.filter_students),
]

# ⭐ MEDIA FILES
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)