from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# from django.http import HttpResponse
# from django.template import loader
 
# Create your views here.


def testPage(request):
    return render(request, 'InspiRy/base.html')

def homePage(request):
    posts = Post.objects.all()
    
    return render(request, 'InspiRy/home.html', {'posts':posts})

def posts_page(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post' : post}
    return render(request, 'InspiRy/posts.html', context)

def footerPage(request):
    return render(request, 'InspiRy/footer.html')

def navigationPage(request):
    return render(request, 'InspiRy/navbar.html')

@login_required(login_url='/InspiRy/login.html')
def userprofilePage(request):
    user = request.user.username
    context = { 'user' : user}
    return render(request, 'InspiRy/profile.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('testPage')
        else:
            messages.error(request, 'Invalid username or password!')
    return render(request, 'InspiRy/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Logout successful!')
    return redirect('/')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('/register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('/register')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('/register')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Your Account was successfully")
        user = authenticate(username=username, password=password)
        return redirect('/')
    
    return render(request, 'Inspiry/register.html')  

# for post in Post.objects.all():
#         print(post.title)
        

