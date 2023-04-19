from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .models import Post
from .froms import PostForm, CustomUserCreationForm

def get_home(request):
    posts = Post.objects.order_by('-created_at')[:9]
    print(posts)
    context = {
        'posts': posts,
    }
    return render(request, 'home.html', context)

def get_about(request):
    return render(request, "about.html")

def logout_view(request):
    logout(request)
    return redirect('/')

def blog_detail(request, pk):
    blog = get_object_or_404(Post, id=pk)
    return render(request, 'blog-details.html', {'blog': blog})

def login_view(request):
    if request.user.id:
        return redirect('/list-blogs/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/') # replace 'home' with the name of your home page url
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html', {})


def signup_view(request):
    if request.user.id:
        return redirect('/list-blogs/')
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        try:
            if form.is_valid():
                user = form.save()
                # Log in the user
                login(request, user)
                messages.success(request, 'Your account has been created!')
                return redirect('/list-blogs/') # replace 'home' with the name of your home page url
            else:
                return render(request, 'signup.html', {"error": form.errors})
        except Exception as e:
            return render(request, 'signup.html', {"error": e})
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {})

@login_required
def create_blog(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        ext = request.FILES['image'].name.split('.')[-1]
        if not ext in ['jpeg', 'jpg']:
            return render(request, 'update-blog.html', {"post": post, "error": "Please upload valid image"})
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Your post has been created!')
            return redirect('/list-blogs/') # replace 'home' with the name of your home page url
        else:
            print(form.errors)
            return render(request, 'create-blog.html',{"errors":form.errors})
    else:
        form = PostForm()
    return render(request, 'create-blog.html',{})

@login_required
def list_blogs(request):
    posts = Post.objects.filter(user=request.user)
    return render(request, 'blogs.html', {'posts': posts})

@login_required
def update_blog(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        ext = request.FILES['image'].name.split('.')[-1]
        if not ext in ['jpeg', 'jpg']:
            return render(request, 'update-blog.html', {"post": post, "error": "Please upload valid image"})
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Your post has been updated!')
            return redirect('/list-blogs/')
        else:
            return render(request, 'update-blog.html', {"post": post, "error":form.errors})
    else:
        return render(request, 'update-blog.html', {"post": post})

@login_required
def delete_blog(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.success(request, 'Your post has been deleted!')
    return redirect('/list-blogs/')

@login_required
def settings(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/list-blogs/')
        else:
            return render(request, 'settings.html', {"error":form.errors})
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'settings.html', {})