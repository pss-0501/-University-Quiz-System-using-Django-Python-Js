from django.urls import path
from prof.views.result import *

urlpatterns = [
    path('exam/<int:exam_id>/scores/', view_exam_scores, name='view_exam_scores'),
    path('exam/results/', view_exam_results, name='view_exam_results'),
    # Add other URLs as needed
]