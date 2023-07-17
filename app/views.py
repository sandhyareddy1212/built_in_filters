from django.shortcuts import render
import datetime

# Create your views here.
def filters(request):
    dt=datetime.datetime.now()
    d={'data':'Sunday is Funday','c':1,'dt':'dt'}
    return render(request,'filters.html',d)
