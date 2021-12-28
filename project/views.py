from django.shortcuts import render, redirect
from .forms import QuestionForm, OptionForm
from .models import Question, Option


def index(request):
    model_question = Question.objects.all()
    model_option = Option.objects.all()
    context = {'model_questions': model_question, 'model_options': model_option}
    return render(request, 'index.html', context)


def create(request):
    form_question = QuestionForm()
    form_option = OptionForm()
    if request.method == "POST":
        form_question = QuestionForm(request.POST or None)
        if form_question.is_valid():
            form_question.save()
            return redirect('create')
        else:
            form_question = QuestionForm()
    if request.method == 'POST':
        form_option = OptionForm(request.POST or None)
        if form_option.is_valid():
            form_option.save()
            return redirect('create')
        else:
            form_option = OptionForm()
    context = {'form_question': form_question, 'form_option': form_option}
    return render(request, 'create.html', context)


def vote(request, pk):
    model_question = Question.objects.get(id=pk)
    options = model_question.choices.all()
    if request.method == 'POST':
        input_value = request.POST.get('choice')
        selected_option = options.get(id=input_value)
        selected_option.vote += 1
        selected_option.save()
    return render(request, 'vote.html', {'model_questions': model_question, 'options': options})


def results(request, pk):
    model_question = Question.objects.get(id=pk)
    options = model_question.choices.all()
    return render(request, 'results.html', {'model_question': model_question, 'options': options})

def delete(request, pk):
    model_question = Question.objects.filter(id=pk)
    model_question.delete()
    return redirect('/')