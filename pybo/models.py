from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User



class Question(models.Model):
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    imgfile = models.ImageField(null=True, upload_to="", blank=True)  # 이미지 컬럼 추가


    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

