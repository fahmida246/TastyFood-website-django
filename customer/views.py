from django.shortcuts import render, redirect
from .forms import *

from django.contrib.auth import get_user_model
User = get_user_model()


def getreservation(request):

    form = CreateReservation()
    if request.method == 'POST':
        form = CreateReservation(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

    context = {'form': form}

    return render(request, 'customer/getreservation.html', context)


def productshow(request):
    blogs = food.objects.all()
    context = {'blogs': blogs}

    return render(request, 'customer/productshow.html', locals())


def getfeedback(request):

    la = reservation.objects.get(user=request.user)
    res = feedback.objects.filter(reservation=la)

    return render(request, 'customer/getfeedback.html', locals())


def addtofav(request, id):
    ti = food.objects.get(id=id)
    post = favourite(food=ti, user=request.user)
    post.save()

    return render(request, 'customer/addtofav.html', locals())


def showfav(request):
    blogs = favourite.objects.filter(user= request.user)

    context = {'blogs': blogs}
    return render(request, 'customer/showfav.html', context)

# def showcart(request):
#     blogs = cart.objects.all()

#     context = {'blogs': blogs}
#     return render(request, 'customer/showblog.html', context)

# def liked(request, pk):
#     blog = Blog.objects.get(pk=pk)
#     user = request.user
#     already_liked = Likes.objects.filter(blog=blog, user=user)
#     if not already_liked:
#         liked_post = Likes(blog=blog, user=user)
#         liked_post.save()
#     return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'slug':blog.slug}))


# def showfav(request):
#     blogs = favourite.objects.all()

#     context = {'blogs': blogs}
#     return render(request, 'customer/showblog.html', context)


# def getreservation(request):
#     return render(request, 'customer/getreservation.html', locals())
