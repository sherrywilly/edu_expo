from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from apps.student.forms import StudentRegistrationForm


# Create your views here.
class StudentRegistrationView(View):
    def get(self, request):
        form = StudentRegistrationForm(
            initial={
                'funding_type': "SELF_FINANCE"
            }
        )
        context = {
            'form': form
        }
        return render(request, "student/registration.html", context)

    def post(self, request):
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            context = {
                'form': form
            }
            messages.success(request, "Thank You for Registering. You will receive Entry Pass Soon!")
            return redirect("student_registration")
        else:
            context = {
                'form': form
            }
            return render(request, "student/registration.html", context)
