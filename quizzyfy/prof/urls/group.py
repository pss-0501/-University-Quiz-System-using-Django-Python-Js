from django.urls import path
from . import views
from prof.views.result import *

urlpatterns = [
    path('viewgroups', views.create_student_group, name='view_groups'),
    path('viewgroups/<int:group_id>', views.view_specific_group, name='view_specific_group'),
    path('viewgroups/<int:group_id>/students', views.view_student_in_group, name='view_students_in_group'),
    path('viewgroups/edit_group/<int:group_id>', views.edit_group, name='edit_group'),
    path('viewgroups/delete_group/<int:group_id>', views.delete_group, name='delete_group'),
    path('exam/<int:exam_id>/scores/', view_exam_scores, name='view_exam_scores'),
    path('exam/results/', view_exam_results, name='view_exam_results'),
]