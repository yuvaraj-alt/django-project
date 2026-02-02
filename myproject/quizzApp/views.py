from django.shortcuts import render,redirect
from .models import QuizzModel
# Create your views here.

def QuestionPage(request):
    question = QuizzModel.objects.all()
    score = 0
    if request.method == "POST":
        for q in question:
            selected = request.POST.get(str(q.id))
            if selected == q.answers:
               score +=1
        request.session["score"]=score
        request.session["total"]=question.count()
        return redirect("Res")

    return render(request,"quizzApp/disQuestions.html",{"question":question})

def ResultPage(request):
    score = request.session.get("score",0)
    total = request.session.get("total",0)
    return render(request,"quizzApp/Result.html",{"score":score,"total":total})
