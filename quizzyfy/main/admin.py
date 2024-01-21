from django.contrib import admin
from main.models.question import *
from main.models.question_paper import *
from main.models.exam import *



# Register your models here.
admin.site.register(Question_DB)
admin.site.register(Question_Paper)
admin.site.register(Special_Students)
admin.site.register(Exam_Model)