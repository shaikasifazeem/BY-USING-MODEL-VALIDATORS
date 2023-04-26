from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import *
def insert_student(requset):
    SFO=studentform()
    d={'SFO':SFO}
    if requset.method=='POST':
            SFD=studentform(requset.POST)
            if SFD.is_valid():
                SFD.save()
                
                return HttpResponse('student data inserted successfully!!')
            else:
                return HttpResponse('data is not valid')
    
    return render(requset,'insert_student.html',d)

