from django.shortcuts import render
from pages.models import Posts
from pages.models import BlogPost


def post_list(request):
    return render(request, 'pages/post_list.html', {})


def home(request):
	posts=BlogPost.objects.all()
	return render(request,"home.html",{"posts":posts})

def post_page(request,post_id):
  	post=BlogPost.objects.get(pk=post_id)
  	context= {"post":post }
  	return render(request,"post.html",context)

