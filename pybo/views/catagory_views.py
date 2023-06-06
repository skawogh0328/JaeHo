from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from ..models import Question
from ..forms import QuestionForm, AnswerForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from pybo import models
from ..models import Category
from ..models import Category, Question, Answer
from django.contrib import messages

def category_view(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    question = Question.objects.filter(category=category)
    return render(request, 'category_view.html', {'category': category, 'question': question})