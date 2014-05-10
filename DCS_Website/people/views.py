from django.shortcuts import render
from people.models import Faculty, Student, Staff

# Create your views here.
def faculty_details(request, pk):
	faculty = Faculty.objects.get(id=pk)
	return render(request,'people/faculty_details.html',{'faculty':faculty})

def student_details(request, pk):
	student = Student.objects.get(id=pk)
	return render(request,'people/student_details.html',{'student':student})
	
def staff_details(request, pk):
	staff = Staff.objects.get(id=pk)
	return render(request,'people/staff_details.html',{'staff':staff})