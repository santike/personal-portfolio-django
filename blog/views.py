from django.shortcuts import render, get_object_or_404
from.models import Post
# Create your views here.
def render_posts(request):
  # posts = Post.objects.all()
   total_posts = Post.objects.count()
   posts = Post.objects.order_by("-date")
   return render(request,'posts.html',{'posts':posts,"total_posts": total_posts})

def post_detail(request, post_id):
   post=get_object_or_404(Post,pk=post_id)
   return render(request,'post_detail.html',{"post":post})