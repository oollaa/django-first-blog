#view jest funkcją, która łączy sql z pythonem
from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    post = Post.objects.all()
    return render(request, 'blog/post_list.html', {"posts":post})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
