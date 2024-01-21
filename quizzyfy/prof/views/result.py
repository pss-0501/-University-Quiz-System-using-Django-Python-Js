from django.shortcuts import render
from main.models.results import *
from student.models import StuExam_DB
from django.db.models import Avg

# def view_exam_scores(request, exam_id):
#     # Get the exam
#     #exam = StuExam_DB.objects.filter(pk=exam_id)
#     exam = StuExam_DB.objects.filter(pk=exam_id).values('examname')
#     first_exam = exam[0]  # Get the first dictionary from the queryset
#     examname = first_exam['examname']
#     print(exam)
#     students = StuExam_DB.objects.filter(examname=examname)
#     print(students)
#     #viewExam = StuExam_DB.objects.get(examname=exam.values('examname'), student=student)

#     # Get all scores for the exam
#     #scores = Score.objects.filter(exam=exam)

#     return render(request, 'prof/result/exam_scores.html', {'exam': exam, 'students': students})

def view_exam_scores(request, exam_id):
    # Get the exam
    exam = StuExam_DB.objects.filter(pk=exam_id).first()  # Use first() to get a single instance
    examname = exam.examname

    # Get all students for the exam
    students = StuExam_DB.objects.filter(examname=examname)

    # Calculate average score
    average_score = students.aggregate(Avg('score'))['score__avg']

    # Get top 5 scores
    top_scores = students.order_by('-score')[:5]

    # Get bottom 5 scores
    bottom_scores = students.order_by('score')[:5]

    context = {
        'exam': exam,
        'students': students,
        'average_score': average_score,
        'top_scores': top_scores,
        'bottom_scores': bottom_scores,
    }

    return render(request, 'prof/result/exam_scores.html', context)

def view_exam_results(request):
    # Retrieve all exams (adjust the filter conditions based on your model)
    #exams = Exam.objects.all()
    studentExamList = StuExam_DB.objects.filter(completed=1)

    context = {
        'exams': studentExamList,
        'prof': request.user,  # Assuming you have a user object representing the professor
    }

    return render(request, 'prof/result/exam_results.html', context)
