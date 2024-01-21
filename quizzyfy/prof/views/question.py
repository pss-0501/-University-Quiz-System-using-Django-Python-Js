from django.shortcuts import get_object_or_404, render, redirect
from main.models import *
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.contrib import messages


def add_question(request):
    prof = request.user

    if request.method == 'POST':
        form = QForm(request.POST)
        if form.is_valid():
            question_instance = form.save(commit=False)
            question_instance.professor = prof
            question_instance.save()
            messages.success(request, 'Question added successfully.')
            return redirect('prof:view_all_ques')
        else:
            messages.error(request, 'Error in the form submission. Please check the form.')

    return render(request, 'prof/question/question.html', {
        'question_db': Question_DB.objects.filter(professor=prof),
        'form': QForm(),
        'prof': prof
    })

   
def view_all_ques(request):
    prof = request.user

    if request.method == 'POST':
        Q_No = int(request.POST['qno'])
        sum_ = 1 + Question_DB.objects.filter(professor=prof).count()

        for i in range(Q_No+1, sum_):
            ques = Question_DB.objects.filter(
                professor=prof, qno=int(i)).first()
            ques.qno -= 1
            ques.save()

        sum_ -= 1

        Question_DB.objects.filter(professor=prof, qno=Q_No).delete()

    return render(request, 'prof/question/view_all_questions.html', {
        'question_db': Question_DB.objects.filter(professor=prof), 'prof': prof
    })

    
def edit_question(request, ques_qno):
    prof = request.user
    ques = Question_DB.objects.get(professor=prof, qno=ques_qno)
    
    if request.method == "POST":
        form = QForm(request.POST, instance=ques)
        if form.is_valid():
            form.save()
            return redirect('prof:view_all_ques')

    form = QForm(instance=ques)
    return render(request, 'prof/question/edit_question.html', {
        'ques': ques,
        'form': form,
        'prof': prof,
    })
