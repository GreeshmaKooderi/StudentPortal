from django import forms
from .models import Student

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'standard': forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(
                attrs={
                    'class':'form-control',
                    'type':'date'
                }
            ),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'place': forms.TextInput(attrs={'class':'form-control'}),
            'address':forms.Textarea(attrs={'class':'form-control','rows':3}),
            'uname': forms.TextInput(attrs={'class':'form-control'}),
            'pwrd': forms.PasswordInput(attrs={'class':'form-control'}),
        }
        
        

