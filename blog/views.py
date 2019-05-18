from django.shortcuts import render,get_object_or_404
from blog.models import Post
def index(request):
    news = Post.objects.all()
    return render(request, "news/index.html", {"news": news})
def view(request, slug):
    news = get_object_or_404(Post, slug=slug)
    return render(request, "news/view.html", {"news": news})
# Create your views here.
