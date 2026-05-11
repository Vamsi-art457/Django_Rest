from django.contrib import admin
from django.urls import path
from app1.views import get_students,add_student,get_student,update_student,delete_student
urlpatterns = [
    path('admin/', admin.site.urls),
    path("students/",get_students),
      path("student/<int:id>/",get_student),
    path("addstudent/",add_student),
    path("update/<int:id>/",update_student),
    path("delete/<int:id>/",delete_student)
]
