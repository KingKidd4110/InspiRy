from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import postForm, CommentForm, ContactForm, ProfileForm
from django.db.models import Q
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
# from django.template import loader
 
# Create your views here.


def testPage(request):
    
    post_form = postForm()
    comment_form = CommentForm()
    
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
                try:
                    comment = comment_form.save(commit=False)
                    comment.user = request.user
                    comment.post = Post.objects.get(id=post_id)
                    comment.save()
                
                    comment.post.comments_count += 1
                    comment.post.save()
                except Post.DoesNotExist:
                    pass
                return redirect('testPage')
                
                

        elif 'like_submit' in request.POST:
            post_id = request.POST.get('post_id')
            if post_id:
                try:
                    post = Post.objects.get(id=post_id)
                    if not Like.objects.filter(post=post, user=request.user).exists():
                        Like.objects.create(post=post, user=request.user)
                        post.likes_count += 1
                        post.save()
                except Post.DoesNotExist:
                    pass
                return redirect('testPage')
            
        else:
            return redirect('testPage')

    posts = Post.objects.select_related('user').prefetch_related('comment_set').all()
    return render(request, 'InspiRy/base.html', {
        'posts': posts,
        'username': request.user.username if request.user.is_authenticated else 'Guest',
        'post_form': post_form,
        'comment_form': comment_form,
    })

def homePage(request):
    return render(request, 'InspiRy/home.html')


def postPage(request, pk):
    comment_form = CommentForm()
    post = Post.objects.select_related('user').get(id=pk)
    
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
    
        if 'comment_submit' in request.POST:  # Handle comment creation
            comment_form = CommentForm(request.POST)
            post_id = request.POST.get('post_id')
            if comment_form.is_valid() and post_id:
                try:
                    comment = comment_form.save(commit=False)
                    comment.user = request.user
                    comment.post = Post.objects.get(id=post_id)
                    comment.save()
                    
                    comment.post.comments_count += 1
                    comment.post.save()
                except Post.DoesNotExist:
                    pass
                return redirect('posts', pk=post_id) if post_id else redirect('testPage')# Fetch all fields, optimize user
            
        elif 'like_submit' in request.POST:
            post_id = request.POST.get('post_id')
            if post_id:
                try:
                    post = Post.objects.get(id=post_id)
                    if not Like.objects.filter(post=post, user=request.user).exists():
                        Like.objects.create(post=post, user=request.user)
                        post.likes_count += 1
                        post.save()
                except Post.DoesNotExist:
                    pass
                return redirect('posts', pk=post_id) if post_id else redirect('testPage')
    return render(request, 'InspiRy/posts.html', {
        'post': post,
        'username': request.user.username if request.user.is_authenticated else 'Guest',
        'comment_form': comment_form,
    })

def footerPage(request):
    return render(request, 'InspiRy/footer.html')

def navigationPage(request):
    return render(request, 'InspiRy/navbar.html')

def get_user_post_count(user):
    if isinstance(user, User):
        return Post.objects.filter(user=user).count()
    else:
        return Post.objects.filter(user_id=user).count()


def userprofilePage(request, pk):
    user = User.objects.get(id=pk)
    post_count = get_user_post_count(user)
    posts = user.post_set.all()
        
    
    context = { 'user' : user, 'posts': posts, 'post_count' : post_count }
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
        login(request, user)
        return redirect('/')
    
    return render(request, 'InspiRy/register.html')  




def deletePost(request, pk):
    post = Post.objects.get(id=pk)
    user = request.user
    if request.method == 'POST':
        post.delete()
        return redirect('testPage')
    return render(request, 'InspiRy/delete.html', {'obj':post})


def delete_comment(request, comment_id):
    if not request.user.is_authenticated:
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({'errors': 'Please log in to delete comments.'}, status=403)
        return redirect('login')

    comment = get_object_or_404(Comment, id=comment_id, user=request.user)
    
    if request.method == 'POST':
        post = comment.post
        post_id = post.id if post else None
        comment.delete()
        if post:
            post.comments_count = max(0, post.comments_count - 1)
            post.save()
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # Return the redirect URL for AJAX to handle
            redirect_url = reverse('posts', kwargs={'pk': post_id}) if post_id else reverse('testPage')
            return JsonResponse({'status': 'success', 'redirect': redirect_url}, status=200)
        
        return redirect('posts', pk=post_id) if post_id else redirect('testPage')
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'errors': 'Invalid request method.'}, status=405)
    return redirect('testPage')





def search_posts(request):
    post_form = postForm()
    comment_form = CommentForm()
    query = request.GET.get('q', '').strip()
    posts = Post.objects.select_related('user__profile').prefetch_related('comment_set').all()

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(user__username__icontains=query)
        ).distinct()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return render(request, 'partials/post_list.html', {'posts': posts})  # Partial template
    return render(request, 'InspiRy/base.html', {
        'posts': posts,
        'username': request.user.username if request.user.is_authenticated else 'Guest',
        'post_form': post_form,
        'comment_form': comment_form,
        'search_query': query,
    })


# views.py


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                f"New message from {name} ({email})",  # Subject
                message,  # Message
                email,  # From email
                ['your-email@gmail.com'],  # To email (your email)
                fail_silently=False,
            )
            return redirect('success_page')  # Redirect after success
    else:
        form = ContactForm()
    return render(request, 'InspiRy/contact.html', {'form': form})


def etc_view(request):
    return render(request, 'InspiRy/etc.html')


@login_required
def edit_profile(request):
    # Ensure a Profile exists for the user
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        # Update fields
        profile.bio = request.POST.get('bio', '')
        profile.birthday = request.POST.get('birthday') or None
        profile.social_link = request.POST.get('social_link', '')
        
        # Handle profile picture upload
        if 'profile_picture' in request.FILES:
            profile.profile_picture = request.FILES['profile_picture']
        
        profile.save()
        return redirect('userprofile', pk=request.user.id)
    
    return redirect('testPage')
