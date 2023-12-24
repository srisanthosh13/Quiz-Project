from django.shortcuts import render,redirect
from .forms import My_Quiz
from django.contrib import messages



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
    js_variable = "userScore()"
    return render(request,"result.html",{"js_variable":js_variable})