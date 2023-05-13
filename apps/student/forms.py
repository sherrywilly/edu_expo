from django import forms

from apps.course.models import Department
from apps.school.models import School
from apps.student.models import Stream, Student


class StudentRegistrationForm(forms.ModelForm):
    name = forms.CharField(max_length=100, label="Full Name", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Full Name'
        }
    ))
    mobile_number = forms.CharField(max_length=10, label="Mobile Number", widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': '+91 Mobile Number'
        }
    ))
    date_of_birth = forms.DateField(label="Date of Birth", widget=forms.DateInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Date of Birth',
            'type': 'date',
            'max': '2007-12-31',
            'min': '2000-01-01'
        }
    ))
    email = forms.EmailField(max_length=100, label="Email", widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Enter Email',
            'type': 'email'
        }
    ))
    school = forms.ModelChoiceField(queryset=School.objects.filter(is_active=True), label="School",
                                    widget=forms.Select(
                                        attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Select School'
                                        }
                                    ),
                                    empty_label="--Select School--")
    stream = forms.ModelChoiceField(queryset=Stream.objects.filter(is_active=True), label="Stream",
                                    widget=forms.Select(
                                        attrs={
                                            'class': 'form-control',
                                            'placeholder': 'Select Stream'
                                        },

                                    ),
                                    empty_label="--Select Stream--"
                                    )
    interested_course = forms.ModelChoiceField(queryset=Department.objects.filter(is_active=True),
                                               label="Interested Course",
                                               widget=forms.Select(
                                                   attrs={
                                                       'class': 'form-control',
                                                       'placeholder': 'Select Interested Course'
                                                   }
                                               ))
    funding_type = forms.ChoiceField(choices=(
        ("EDUCATION_LOAN", "Education Loan"),
        ("SELF_FINANCE", "Self Finance"),
    ), label="Funding Type", widget=forms.RadioSelect(
        attrs={
            'placeholder': 'Select Funding Type'
        }
    ))
    interested_course = forms.ModelChoiceField(queryset=Department.objects.filter(is_active=True),
                                               label="Interested Course",
                                               widget=forms.Select(
                                                   attrs={
                                                       'class': 'form-control',
                                                       'placeholder': 'Select Interested Course'
                                                   }
                                               ),
                                               empty_label="--Select Interested Course--"
                                               )

    class Meta:
        model = Student
        exclude = ('created_at', 'updated_at')
