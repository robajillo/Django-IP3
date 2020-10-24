from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



def home(request):
    post = Post.get_posts()
    ratings = Rating.get_ratings(id)
    profile = Profile.get_profile()

    current_user = request.user
    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            rating = form.save(commit=False)
            rating.post = post
            rating.user = current_user
            rating.design = design
            rating.usability = usability
            rating.content = content
            rating.save()
        return redirect('home')

    else:
        form = RatingsForm()

    return render(request,"home.html",{"post":post, "ratings":ratings,"form": form,"profile":profile})

@login_required(login_url='/accounts/login/')
def profile(request,profile_id):

    profile = Profile.objects.get(pk = profile_id)
    posts = Post.objects.filter(profile_id=profile).all()

    return render(request,"profile.html",{"profile":profile,"posts":posts})

@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('home')

    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})
