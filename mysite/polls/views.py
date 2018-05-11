from django.shortcuts import render

# Create your views here.
from django.views import View

from .models import Question

def index(request):
    return render(request, 'polls/index.html')


class PollQuestions(View):
    title = "Questions"
    template = 'polls/questions.html'

    def get(self, request):
        questions = list(Question.objects.values('pk', 'question_text'))

        context = {
            'question_text': self.title,
            'props': questions,
        }

        return render(request, self.template, context)
