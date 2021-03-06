from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *

# Create your views here.

def index(request):
    categories = Category.objects.all()
    restaurants = Restaurant.objects.all()
    content = {'categories' : categories, 'restaurants':restaurants}
    return render(request, 'shareRes/index.html', content)
    # return HttpResponse("index")

def restaurantDetail(request):
    return render(request, 'shareRes/restaurantDetail.html')
    # return HttpResponse("restaurantDetail")

def restaurantCreate(request):
    return render(request, 'shareRes/restaurantCreate.html')
    # return HttpResponse("restaurantCreate")

def categoryCreate(request):
    categories = Category.objects.all()
    content = {"categories":categories}    
    return render(request, 'shareRes/categoryCreate.html', content)
    # return HttpResponse("categoryCreate")
def Create_category(request):
    category_name = request.POST['categoryName']
    new_category = Category(category_name=category_name)
    new_category.save()
    return HttpResponseRedirect(reverse('index'))
    # return HttpResponse("여기서 category Create 기능을 구현할 거야")

def Delete_category(request):
    category_id = request.POST['categoryId']
    delete_category = Category.objects.get(id=category_id)
    delete_category.delete()
    return HttpResponseRedirect(reverse('cateCreatePage'))

def restaurantCreate(request):
    categories = Category.objects.all()
    content = {"categories" : categories}
    return render(request, 'shareRes/restaurantCreate.html', content)
def Create_restaurant(request):
    category_id = request.POST['resCategory']
    category = Category.objects.get(id = category_id)
    name = request.POST['resTitle']
    link = request.POST['resLink']
    content = request.POST['resContent']
    keyword = request.POST['resLoc']
    new_res = Restaurant(category = category, restaurant_name=name,
    restaurant_link = link, restaurant_content = content, restaurant_keyword = keyword)
    new_res.save()
    return HttpResponseRedirect(reverse('index'))

def restaurantDetail(request,res_id):
    restaurant = Restaurant.objects.get(id = res_id)
    content = {'restaurant':restaurant}
    return render(request, 'shareRes/restaurantDetail.html', content)

def restaurantUpdate(request, res_id):
    categories = Category.objects.all()
    content = {'categories' : categories}
    return render(request, 'shareRes/restaurantUpdate.html', content)
 