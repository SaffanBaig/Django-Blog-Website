from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        "posted_by":"Saffan",
        "description":"Our first post",
        "posted_date":"May-17-19",
        "title":"first Post"
    },
    {
        "posted_by":"Hassan",
        "description":"Our second post",
        "posted_date":"May-17-19",
        "title":"Second Post"
    }
]
def home(request):
    context = {
        "posts":posts
    }
    return render(request,'mainpage/home.html', context)

def about(request):
    context = {
        "title":"about"
    }
    return render(request,'mainpage/about.html', context)