from django.shortcuts import render ,redirect
from .models import Posts 
from .forms import Postfrom
from django.urls import reverse

# Create your views here.

def post_list(request):
    objects = Posts.objects.all()
    return render(request,'posts/post_list.html',{"posts":objects})


def post_detail(request , id):
    single = Posts.objects.get(id=id)
    return render(request,'posts/post_detail.html',{"posts":single})

def new_post(request):
    if request.method == "POST":
        form = Postfrom(request.POST , request.FILES)
        if form.is_valid():
           my_form = form.save(commit=False)
           my_form.author = request.user
           my_form.save()
           return redirect(reverse('posts:post_list'))
       
    else:
        form = Postfrom
    return render(request,'posts/new.html',{'form':form})
    
    
    

def edit_post(request,id):
    single = Posts.objects.get(id=id)
    if request.method == "POST":
        form = Postfrom(request.POST , request.FILES ,instance=single)
        if form.is_valid():
            form.save()
    else:
        form = Postfrom(instance=single)
    return render(request,'posts/edit.html',{'form':form})
       
     
     
def delete_post(request,id):
    single = Posts.objects.get(id=id)
    single.delete()
    return redirect(reverse('posts:post_list'))