from django.shortcuts import render
from people.models import Faculty, Student, Staff

# Create your views here.
def pipz(request):
    """Fetch the requested objects with the given primary keys from the database,
    create context by assigning the objects to corresponding variables in the template,
    and render the page using the context and the template in the given directory.
    """
    faculty_list = Faculty.objects.order_by('-position')
    student_list = Student.objects.order_by('-org_name')
    staff_list = Staff.objects.order_by('-last_name')
    
    faculty_assistant_list = Faculty.objects.filter(position__startswith='Assistant').order_by('last_name')
    faculty_associate_list = Faculty.objects.filter(position__startswith='Associate').order_by('last_name')
    faculty_instructor_list = Faculty.objects.filter(position__startswith='Instructor').order_by('last_name')
    
    pipz_context = {'faculty_list' : faculty_list,
                    'student_list' : student_list,
            'staff_list' : staff_list,
            'faculty_instructor_list' : faculty_instructor_list,
            'faculty_assistant_list' : faculty_assistant_list,
            'faculty_associate_list' : faculty_associate_list}
    return render(request, 'people/people.html', pipz_context)