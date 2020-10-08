from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def test(request):
    return HttpResponse('测试成功')

@csrf_exempt
def get_data(request):
    print(request.GET)
    print(request.POST)
    return HttpResponse('数据获取成功')