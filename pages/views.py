from django.shortcuts import render,HttpResponse
from pages.models import Posts
from pages.models import BlogPost

def post_list(request):
	posts=Posts.objects.all()
	# myposts = Posts.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request,"blog/post_list.html",{"post":posts})


def home(request):
	posts=BlogPost.objects.all()
	return render(request,"home.html",{"posts":posts})

def post_page(request,post_id):
	post=BlogPost.objects.get(pk=post_id)
	context= {"post":post }
	return render(request,"post.html",context)

