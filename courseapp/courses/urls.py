from django.urls import path
from . import views

#http://127.0.0.1:8000/client    => anasayfa
#http://127.0.0.1:8000/client/home      => anasayfa
#http://127.0.0.1:8000/client/kurslar   =>Kurs listesi


urlpatterns = [
    path('',views.index, name="index"),
    path('search',views.search, name="search"),
    path('create-course',views.create_course, name="create_course"),
    path('course-list',views.course_list,name="course_list"),
    path('course-edit/<int:id>', views.course_edit,name="course_edit"),
    path('course-delete/<int:id>', views.course_delete,name="course_delete"),
    path('upload',views.upload, name="upload_image"),
    path('<slug:slug>', views.Details, name="course_details"),
    path('kategori/<slug:slug>',views.getCoursesByCategory , name='courses_by_category'),    #Değişken pathler her zaman en alt kısımda bulunmalıdır,çünkü üstte oldugu zaman sıralama kaynaklı hata alınabilir.
    
]
