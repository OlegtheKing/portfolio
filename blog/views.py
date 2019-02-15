from django.shortcuts import render, get_object_or_404  # either finds object in db or throws 404 error
from .models import Blog

def allblogs(request):
    blogs = Blog.objects
    return render(request, "blog/allblogs.html", {"blogs": blogs})  # need to specify directory

def detail(request, blog_id):
    detailblog = get_object_or_404(Blog, pk=blog_id)  # pk = primary key
    return render(request, "blog/detail.html", {"detailblog":detailblog})