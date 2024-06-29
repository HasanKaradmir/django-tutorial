from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blog, Category

data = {
    "blogs": [
        {
            "id": 1,
            "title": "Komple Web Geliştirme Kursu",
            "image": "1.jpg",
            "is_active": True,
            "is_home": False,
            "description": "Cok iyi bir kurs"
            },
        {
            "id": 2,
            "title": "Python Kursu",
            "image": "2.jpg",
            "is_active": True,
            "is_home": True,
            "description": "Cok iyi bir kurs"
            },
        {
            "id": 3,
            "title": "Django Kursu",
            "image": "3.jpg",
            "is_active": False,
            "is_home": True,
            "description": "Cok iyi bir kurs"
            },
        {
            "id": 4,
            "title": "Node JS Kursu",
            "image": "4.jpg",
            "is_active": True,
            "is_home": True,
            "description": "Cok iyi bir kurs"
            },
    ],
}

# Create your views here.

def index(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True, is_home=True),
        "categories": Category.objects.all()
    }
    return render(request, "blog/index.html", context)


def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
                "categories": Category.objects.all()

    }
    return render(request, "blog/blogs.html", context)


def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    
    return render(request, "blog/blog_details.html", {
        "blog": blog,
    })
    
def blogs_by_category(request, slug):
    context = {
        "blogs": Blog.objects.filter(is_active=True, category__slug=slug),
        "categories": Category.objects.all(),
        "selected_category": slug,

    }
    return render(request, "blog/blogs.html", context)
