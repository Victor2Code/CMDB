import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt


def test(request):
    return HttpResponse('测试成功')

@csrf_exempt
def get_data(request):
    # print(request.GET)
    # print(request.POST)
    # print(request.body)  # 请求体不是&符号连接无法通过request.POST获取内容，可以用request.body来检测请求体具体是什么格式
    content = request.body
    content_json = json.loads(content.decode('utf-8'))
    print(content_json)
    return HttpResponse('数据获取成功')