from django.shortcuts import render, get_object_or_404 # オブジェクトの取得 http://djangoproject.jp/doc/ja/1.0/topics/http/shortcuts.html#get-list-or-404
from django.views.generic import TemplateView
from .models import Post

# Create your views here.
def index(request):
    posts = Post.objects.order_by('published')
    return render(request, 'viewApp/index.html', {'posts': posts})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'viewApp/post_detail.html',{'post':post})