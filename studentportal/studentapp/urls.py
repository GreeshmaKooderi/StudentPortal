from django.urls import path
from studentapp.views import *

urlpatterns = [
    
    path('', HomeView.as_view(), name='home'),
    
    path('register',AddStudentView.as_view(),name='reg'),
    
    path('login/', LoginView.as_view(), name='login'),
    
    path(
        'dashboard/<int:id>/',
        StudentDashboardView.as_view(),
        name='dashboard'
    ),

    path(
        'editstudent/<int:id>/',
        EditStudentView.as_view(),
        name='editstudent'
    ),

     path(
        'confirmdelete/<int:id>/',
        ConfirmDeleteStudentView.as_view(),
        name='confirmdelete'
    ),

    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),
]
