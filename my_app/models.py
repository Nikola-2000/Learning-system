from operator import mod
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomUsers(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(upload_to='profile_pics', max_length=100, blank=True)
    world_points = models.IntegerField(null=True)


class Courses(models.Model):
    course_name = models.CharField(max_length = 100, unique=True)
    description = models.CharField(max_length=255, default='This is a test description')
    students = models.ManyToManyField(CustomUsers, null=True)
    cover_photo = models.ImageField(upload_to='cover_photos', blank=True)

class Lesson(models.Model):
    titles = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    course_lesson = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True)

class Tests(models.Model):
    question_title = models.CharField(max_length=500)
    correct_answers = models.CharField(max_length=1000)
    for_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True)
    for_course = models.ForeignKey(Courses, on_delete=models.CASCADE, null=True)

class UserAnswers(models.Model):
    answers = models.CharField(max_length=1000)
    user = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)
    for_test = models.ForeignKey(Tests, on_delete=models.CASCADE, null=True)

class MessagesSender(models.Model):
    content = models.CharField(max_length=1000)
    sender = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)

class MessagesReciever(models.Model):
    content = models.CharField(max_length=1000)
    reciever = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)

class GroupChat(models.Model):
    content = models.CharField(max_length=1000)
    members = models.ManyToManyField(CustomUsers)

class Chat(models.Model):
    content_from_sender = models.ForeignKey(MessagesSender, on_delete=models.CASCADE, null=True)
    content_from_reciever = models.ForeignKey(MessagesReciever, on_delete=models.CASCADE, null=True)
    users = models.ForeignKey(CustomUsers, on_delete=models.CASCADE)