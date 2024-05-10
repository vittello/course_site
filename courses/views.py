from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from .models import Course, Lesson, Comment
from .forms import CourseAddForm, CommentForm
from django.contrib import messages
from django.urls import reverse
from django.http import JsonResponse

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

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(CourseDetailView, self).get_context_data(**kwargs)
        course = Course.objects.filter(slug=self.kwargs['slug']).first()
        ctx['title'] = course
        ctx['lessons'] = Lesson.objects.filter(course=course).order_by('number')
        return ctx
    
    
class LessonDetailView(DetailView):
    model = Lesson
    template_name = 'courses/lesson-detail.html'
    slug_url_kwarg = 'lesson_slug'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        lesson = self.get_object()  
        comments = Comment.objects.filter(lesson=lesson)

        if lesson.video:
            lesson.video = lesson.video.split("=")[1]


        ctx['form'] = CommentForm()
        ctx['title'] = lesson
        ctx['lesson'] = lesson
        ctx['comments'] = comments 
        return ctx
    
    

    def post(self, request, *args, **kwargs):
        lesson_slug = self.kwargs.get('lesson_slug')
        lesson = Lesson.objects.get(slug=lesson_slug)
        
        post = request.POST.copy()
        post['author'] = request.user
        post['lesson'] = lesson
        request.POST = post
        
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.lesson = lesson
            comment.author = request.user
            comment.save()
    

        url = self.kwargs['slug'] + '/' + self.kwargs['lesson_slug']
        return redirect('/courses/' + url)


    
def payment(request):
    return render(request, 'courses/payment.html')
    