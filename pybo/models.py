from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name



class Question(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE,
                                 related_name='category_question', default=1)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE,
                               related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    imgfile = models.ImageField(null=True, blank=True, upload_to="")  # 이미지 컬럼 추가
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')
