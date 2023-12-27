from django.shortcuts import render,redirect
from .forms import My_Quiz
from django.contrib import messages
from .models import Quiz_Registration_Form




# Create your views here.
def home(request):
    return render(request, "home.html")

def register(request):
    if request.method == 'POST':
        form = My_Quiz(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request,"Registered Successfull...")
                return redirect("Quiz")
            except:
                pass
    else:
        form = My_Quiz()
        return render(request,"registerform.html", {'form':form})
    
def quiz(request):
    return render(request,"quiz.html")

def result(request):
    scores = Quiz_Registration_Form.objects.all()
    if (scores):
        return render(request, 'result.html', {'scores': scores})
    else:
        return render(request, 'result.html')