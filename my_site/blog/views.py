from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Abayomi',
        'title': 'Blog Post 1',
        'content': 'First post for website',
        'date_posted': 'May 4, 2021'
    },
    {
        'author': 'Yuka',
        'title': 'Blog Post 2',
        'content': 'Second post for website',
        'date_posted': 'May 5, 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


