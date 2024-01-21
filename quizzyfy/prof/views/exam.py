from django.shortcuts import get_object_or_404, render, redirect
from main.models import *
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

def view_exams(request):
    prof = request.user

    new_Form = ExamForm()
    new_Form.fields["student_group"].queryset = Special_Students.objects.filter(
        professor=prof)
    new_Form.fields["question_paper"].queryset = Question_Paper.objects.filter(
        professor=prof)

    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            exam = form.save(commit=False)
            exam.professor = prof
            exam.save()
            form.save_m2m()
            return redirect('prof:view_exams')

    exams = Exam_Model.objects.filter(professor=prof)

    return render(request, 'prof/exam/view_exams.html', {
        'exams': exams, 'examform': new_Form, 'prof': prof,
    })
    

def view_exam(request, exam_id):
    prof = request.user
    exam = Exam_Model.objects.get(professor=prof, pk=exam_id)
    return render(request, 'prof/exam/view_exam.html', {
        'exam': exam, 'prof': prof, 'student_group': exam.student_group.all()
    })
    

def edit_exam(request, exam_id):
    prof = request.user
    exam = get_object_or_404(Exam_Model, professor=prof, pk=exam_id)

    form = ExamForm(instance=exam)
    form.fields["student_group"].queryset = Special_Students.objects.filter(professor=prof)
    form.fields["question_paper"].queryset = Question_Paper.objects.filter(professor=prof)

    if request.method == 'POST':
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()
            return redirect('prof:view_exams')

    return render(request, 'prof/exam/edit_exam.html', {
        'examform': form,
        'exam': exam,
        'prof': prof
    })
    

def delete_exam(request, exam_id):
    prof = request.user
    exam = Exam_Model.objects.get(professor=prof, pk=exam_id)
    exam.delete()
    return redirect('prof:view_exams')