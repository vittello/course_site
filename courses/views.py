from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from .models import Course
from .forms import CourseAddForm

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'
    ordering = ['-id']
    
    def get_context_data(self, **kwargs):
        ctx = super(CourseListView, self).get_context_data(**kwargs)
        ctx['title'] = 'Главная страница сайта!'
        return ctx

class CourseAddView(CreateView):
    model = Course
    form_class = CourseAddForm  
    template_name = 'courses/add_course.html'
    success_url = '/courses/'
    
class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'  
    context_object_name = 'course'
    
def payment(request):
    return render(request, 'courses/payment.html')
    