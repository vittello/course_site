from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Course(models.Model):
    # slug, title, desc, image
    slug = models.SlugField('Уникальное название курса')
    title = models.CharField('Название курса', max_length=120)
    desc = models.TextField('Описание курса')
    image = models.ImageField('Изображение', default='default.png', upload_to='course_images')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('course_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        
class Lesson(models.Model):
    
    slug = models.SlugField('Уникальное название урока')
    title = models.CharField('Название урока', max_length=120)
    desc = models.TextField('Описание урока')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Какой курс?')
    number = models.IntegerField('Номер урока')
    video = models.CharField('Видео URL', max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('lesson_detail', kwargs={'slug': self.course.slug, 'lesson_slug': self.slug})



    
    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)  


    def __str__(self):
        return self.text
    
    
    
