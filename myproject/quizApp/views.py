from django.shortcuts import render, redirect
from .models import QuizModel
# Create your views here.

def questionPage(request):
    questions = QuizModel.objects.all()
    score = 0
    if request.method == "POST":
        for q in questions:
            select = request.POST.get(str(q.id))
            if select == q.answers:
                score+=1
        request.session["score"] = score
        request.session["total"] = questions.count()
        return redirect("res")


    return render(request, "quizApp/question.html",{"questions":questions})

def resultPage(request):
    score = request.session.get("score",0)
    total = request.session.get("score",0)
    return render(request, "quizApp/result.html",{"score":score,"total":total})