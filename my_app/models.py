from operator import mod
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='uploads/',height_field=None, width_field=None, max_length=100)
    world_points = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name

class Courses(models.Model):
    course_name = models.CharField(max_length = 100)

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
    user = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)
    for_test = models.ForeignKey(Tests, on_delete=models.CASCADE, null=True)

class MessagesSender(models.Model):
    content = models.CharField(max_length=1000)
    sender = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)

class MessagesReciever(models.Model):
    content = models.CharField(max_length=1000)
    reciever = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)

class GroupChat(models.Model):
    content = models.CharField(max_length=1000)
    members = models.ManyToManyField(Users)

class Chat(models.Model):
    content_from_sender = models.ForeignKey(MessagesSender, on_delete=models.CASCADE, null=True)
    content_from_reciever = models.ForeignKey(MessagesReciever, on_delete=models.CASCADE, null=True)
    users = models.ForeignKey(Users, on_delete=models.CASCADE, null=True)