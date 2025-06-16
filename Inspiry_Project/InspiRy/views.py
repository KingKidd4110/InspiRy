from django.shortcuts import render, redirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import postForm, CommentForm
from django.db.models import Q
from django import forms
# from django.http import HttpResponse
# from django.template import loader
 
# Create your views here.


# def testPage(request):
#     if request.method == 'POST':
#         if not request.user.is_authenticated:
#             return redirect('login')  # Redirect to login if not authenticated
#         form = postForm(request.POST, request.FILES)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.user = request.user
#             post.save()
#             return redirect('testPage')  # Stay on homepage after submission
#     else:
#         form = postForm()
    
#     posts = Post.objects.select_related('user').all()  # Fetch all posts, optimize user
#     return render(request, 'InspiRy/base.html', {
#         'posts': posts,
#         'username': request.user.username if request.user.is_authenticated else 'Guest',
#         'form': form  # Pass form to modal
#     })
    
# views.py

def testPage(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')  # Redirect to login if not authenticated

        if 'post_submit' in request.POST:  # Handle post creation
            post_form = postForm(request.POST, request.FILES)
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect('testPage')

        elif 'comment_submit' in request.POST:  # Handle comment creation
            comment_form = CommentForm(request.POST)
            post_id = request.POST.get('post_id')
            if comment_form.is_valid() and post_id:
                comment = comment_form.save(commit=False)
                comment.user = request.user
                comment.post = Post.objects.get(id=post_id)
                comment.save()
                # Update comments_count
                comment.post.comments_count += 1
                comment.post.save()
                return redirect('testPage')

        elif 'like_submit' in request.POST:  # Handle like action
            post_id = request.POST.get('post_id')
            if post_id:
                post = Post.objects.get(id=post_id)
                post.likes_count += 1
                post.save()
                return redirect('testPage')

    else:
        post_form = postForm()
        comment_form = CommentForm()

    posts = Post.objects.select_related('user').prefetch_related('comment_set').all()
    return render(request, 'InspiRy/base.html', {
        'posts': posts,
        'username': request.user.username if request.user.is_authenticated else 'Guest',
        'post_form': post_form,
        'comment_form': comment_form,
    })

def homePage(request):
    return render(request, 'InspiRy/home.html')

# def posts_page(request, pk):
#     post = Post.objects.get(id=pk)
#     context = {'post' : post}
#     return render(request, 'InspiRy/posts.html', context)

def postPage(request, pk):
    post = Post.objects.select_related('user').get(id=pk)  # Fetch all fields, optimize user
    return render(request, 'InspiRy/posts.html', {
        'post': post,
        'username': request.user.username if request.user.is_authenticated else 'Guest'
    })

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
    
    return render(request, 'InspiRy/register.html')  

# for post in Post.objects.all():
#         print(post.title)




def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('testPage')
    return render(request, 'InspiRy/delete.html', {'obj':post})
    


# class PostForm(forms.Form):
#     content = forms.CharField(widget=forms.Textarea(attrs={
#         'class': 'w-full bg-transparent border-0 resize-none focus:ring-0 text-xl placeholder-gray-500 min-h-[100px]',
#         'placeholder': "What's happening?",
#         'rows': 3
#     }), required=False)
#     media = forms.ImageField(required=False)

# def create_post(request):
#     media_preview_url = None
#     post_button_disabled = True
    
#     if request.method == 'POST':
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Process the post (save to database, etc.)
#             return redirect('testPage')  # Redirect after successful post
    
#     else:
#         form = PostForm()
    
#     # Check if form has content to enable/disable button
#     if 'content' in request.POST and request.POST['content'].strip() != '':
#         post_button_disabled = False
#     elif 'media' in request.FILES:
#         post_button_disabled = False
    
#     # Handle media preview
#     if 'media' in request.FILES:
#         media_preview_url = request.FILES['media'].temporary_file_path()
    
#     return render(request, 'InspiRy/create.html', {
#         'form': form,
#         'media_preview_url': media_preview_url,
#         'post_button_disabled': post_button_disabled
#     })
