from django.shortcuts import render,redirect
from django.views import View
from studentapp.forms import *
from studentapp.models import Student

from django.contrib import messages

from django.contrib.auth import authenticate,login,logout

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class AddStudentView(View):
    def get(self,request):
        studentForm = StudentForm()
        return render(request,"registration.html",{'form':studentForm})
    
    def post(self,request):
        form_data = StudentForm(data=request.POST,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
        return render(request,'home.html')
    

from django.contrib import messages

class LoginView(View):

    def post(self, request):

        uname = request.POST.get('uname')
        pwrd = request.POST.get('pwrd')

        student = Student.objects.filter(
            uname=uname,
            pwrd=pwrd
        ).first()

        if student:
            request.session['student_id'] = student.id

            messages.success(
                request,
                f"Welcome {student.name}!"
            )

            return redirect(
                'dashboard',
                id=student.id
            )

        messages.error(
            request,
            "Invalid Username or Password"
        )

        return redirect('home')
        
        
class StudentDashboardView(View):

    def get(self, request, id):
        student = Student.objects.get(id=id)

        return render(
            request,
            'studentDashboard.html',
            {'student': student}
        )
        
        


class EditStudentView(View):

    def get(self, request, id):

        student = Student.objects.get(id=id)

        form = StudentForm(instance=student)

        return render(
            request,
            'editStudent.html',
            {'form': form}
        )

    def post(self, request, id):

        student = Student.objects.get(id=id)

        form = StudentForm(
            request.POST,
            request.FILES,
            instance=student
        )

        if form.is_valid():
            form.save()
            return redirect('dashboard', id=id)

        return render(
            request,
            'editStudent.html',
            {'form': form}
        )
        
class ConfirmDeleteStudentView(View):

    def get(self, request, id):

        student = Student.objects.get(id=id)

        return render(
            request,
            'confirmDelete.html',
            {'student': student}
        )

    def post(self, request, id):

        student = Student.objects.get(id=id)

        student.delete()

        request.session.flush()

        return redirect('home')
    
    
    
class LogoutView(View):

    def get(self, request):

        request.session.flush()

        return redirect('home')