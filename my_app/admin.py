from django.contrib import admin
from .models import CustomUsers, Courses, Chat,  GroupChat, Lesson, UserAnswers, Tests, MessagesSender, MessagesReciever

# Register your models here.
admin.site.register(CustomUsers)
admin.site.register(Courses)
admin.site.register(Chat)
admin.site.register(GroupChat)
admin.site.register(Lesson)
admin.site.register(UserAnswers)
admin.site.register(Tests)
admin.site.register(MessagesSender)
admin.site.register(MessagesReciever)

