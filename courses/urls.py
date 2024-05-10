from django.urls import path
from . import views

urlpatterns = [
    path('', views.CourseListView.as_view(), name='courses'),
    path('add_course/', views.CourseAddView.as_view(), name='add_course'),
    path('<slug:slug>/', views.CourseDetailView.as_view(), name='course-detail'), 
    path('payment/', views.payment, name='payment'),
    path('<slug:slug>/<slug:lesson_slug>/', views.LessonDetailView.as_view(), name='lesson_detail')
]
