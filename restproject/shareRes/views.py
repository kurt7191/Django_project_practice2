from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'shareRes/index.html')
    # return HttpResponse("index")

def restaurantDetail(request):
    return render(request, 'shareRes/restaurantDetail.html')
    # return HttpResponse("restaurantDetail")

def restaurantCreate(request):
    return render(request, 'shareRes/restaurantCreate.html')
    # return HttpResponse("restaurantCreate")

def categoryCreate(request):
    return render(request, 'shareRes/categoryCreate.html')
    # return HttpResponse("categoryCreate")


    
# def restaurantDetail(request):
#     return HttpResponse('restaurantDetail')

# def restaurantCreate(request):
#     return HttpResponse('restaurantCreate')

# def restaurantUpdate(request):
#     return HttpResponse('restaurantUpdate')


# def Delete_restaurant(request):
#     return HttpResponse('Delete_restaurant')
