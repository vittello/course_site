from django.urls import path
from . import views




urlpatterns = [
    path('', views.CourseListView.as_view(), name='courses'),
    path('add_course/', views.CourseAddView.as_view(), name='add_course'),
    path('courses/<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('payment', views.payment, name='payment'),
]