from django import forms
from students import models

class student_model_form(forms.ModelForm):
    class Meta:
        model = models.students
        fields = "__all__"