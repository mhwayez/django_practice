from django.shortcuts import render
from django.http import HttpResponse
from students.models import students
from students import forms

def home(request):
    return HttpResponse("Hello World")


def wayez_details(request):
    return HttpResponse("এপ থেকে বলছি মাগো !!! ")

def template_wayez(request):
    student_list = students.objects.order_by('name')
    diction = {'students': student_list}
    return render(request,'students/index.html',context=diction)

def form(request):
    student_form= forms.student_model_form()

    if request.method == "POST":
        student_form = forms.student_model_form(request.POST)

        if student_form.is_valid():
            student_form.save(commit=True)
            return template_wayez(request)



    diction = {'test_key':student_form}
    return render(request, 'students/form.html', context=diction)