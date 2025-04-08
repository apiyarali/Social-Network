import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from .models import User, Post
from . import forms

# Paginator 
def paginator(posts, page):
    paginator = Paginator(posts, 10)
    page_number = page
    page_obj = paginator.get_page(page_number)

    return page_obj 

# All Post
def index(request):
    allPost = Post.objects.filter().order_by("-created").all()

    return render(request, "network/index.html",{
        "posts": allPost,
        "form":forms.PostForm(),
        "page_obj": paginator(allPost, request.GET.get('page')),
    })

# New Post
@login_required(login_url="login")
def new(request):
    if request.method == "POST":
        form = forms.PostForm(request.POST)
        if form.is_valid():
            posts = form.save(commit=False)
            posts.post = form.cleaned_data['post']
            posts.user = request.user
            posts.save()
            
    return HttpResponseRedirect(reverse("index"))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

# Profile View 
@login_required(login_url="login")
def profile(request):
    profilePost = Post.objects.filter(user=request.user).order_by("-created").all()

    # Following / followers count
    following = request.user.followers.all().count()
    follower = request.user.following.all().count()

    return render(request, "network/profile.html",{
        "posts": profilePost,
        "form":forms.PostForm(),
        "page_obj": paginator(profilePost, request.GET.get('page')),
        "following": following,
        "follower": follower
    })

# Follow / unfollow
@login_required(login_url="login")
def follow(request, user_id):
    currUser = User.objects.get(id=request.user.id)
    postUser = User.objects.get(id=user_id)

    if request.user.is_authenticated:
        if request.method == "POST":
            if currUser != postUser:
                if postUser not in currUser.followers.all():
                    currUser.followers.add(postUser)
                else:
                    currUser.followers.remove(postUser)
    
    return redirect(request.META['HTTP_REFERER'])

# Display post for particular user - by clicking on user name
@login_required(login_url="login")
def userPosts(request, user_id):
    userPost = Post.objects.filter(user=user_id).order_by("-created").all()
    postUser = User.objects.get(id=user_id)

    # Following / followers count
    following = postUser.followers.all().count()
    follower = postUser.following.all().count()

    return render(request, "network/userPosts.html",{
        "postUser": postUser,
        "posts": userPost,
        "form":forms.PostForm(),
        "page_obj": paginator(userPost, request.GET.get('page')),
        "following": following,
        "follower": follower
    })

# Following view
def followingView(request):
    followPost = Post.objects.filter(user__in=request.user.followers.all()).order_by("-created").all()

    return render(request, "network/following.html",{
        "posts": followPost,
        "form":forms.PostForm(),
        "page_obj": paginator(followPost, request.GET.get('page'))
    })

# Like API
@csrf_exempt
@login_required(login_url="login")
def like(request, post_id):
    try:
        likePost = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)    

    likeToggle=False

    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user not in likePost.like.all():
                likePost.like.add(request.user)
                likes =  likePost.like.count()
                likeToggle = True
                return JsonResponse({"add": "You like this post","likes": likes, "likeToggle": likeToggle}, status=200)
            else:
                likePost.like.remove(request.user)
                likes =  likePost.like.count()
                return JsonResponse({"delete": "You dislike this post","likes": likes, "likeToggle": likeToggle}, status=200)
        else:
            return JsonResponse({"error": "POST request required"}, status=400)    
    else:
        return JsonResponse({"error": "User must be logged in"}, status=400)    

# Edit post API
@csrf_exempt
@login_required(login_url="login")
def edit(request, post_id):
    try:
        editPost=Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found."}, status=404)  
    
    if request.user != editPost.user:
        return JsonResponse({"error": "Unauthorized user"}, status=401) 
    
    if request.method == "POST":
        data = json.loads(request.body)
        editPost = Post.objects.get(id=post_id)
        editPost.post = data.get("content")
        editPost.save()
        return JsonResponse({"update": "Post has been updated"}, status=200)
    else:
        return JsonResponse({"error": "POST request required"}, status=400)     
