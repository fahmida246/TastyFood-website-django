from django.shortcuts import render, redirect
from .forms import *
from customer.models import reservation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
User = get_user_model()


@login_required
def addfood(request):
    form = CreateFoodForm()
    if request.method == 'POST':
        form = CreateFoodForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

    context = {'form': form}

    return render(request, 'company/addfood.html', context)


@login_required
def addblog(request):
    form = CreateBlog()
    if request.method == 'POST':
        form = CreateBlog(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/showblog')

    return render(request, 'company/addblog.html', locals())


@login_required
def showfood(request):
    blogs = food.objects.all()

    context = {'blogs': blogs}

    return render(request, 'company/showfood.html', locals())


@login_required
def showblog(request):
    blogs = blog.objects.all()

    context = {'blogs': blogs}
    return render(request, 'company/showblog.html', context)


@login_required
def getresponse(request):
    blogs = reservation.objects.all()

    context = {'blogs': blogs}
    return render(request, 'company/getresponse.html', locals())


@login_required
def addfeedback(request, id):
    res = reservation.objects.get(id=id)
    form = CreateFeedback()
    if request.method == 'POST':
        form = CreateFeedback(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.reservation = res
            post.save()

    context = {'form': form}
    # res = reservation.objects.get(id=id)
    # form = CreateFeedback()
    # if request.method == 'POST':
    #     print(res)
    #     form = CreateFeedback(request.POST)
    #     if form.is_valid():
    #         form.user = request.user
    #         form.reservation = res
    #         form.save()

    return render(request, 'company/addfeedback.html', locals())
