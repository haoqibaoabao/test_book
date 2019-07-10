from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# 1. 定义视图函数，HttpRequest
# 2. 进行url配置，建立url地址和视图之间的对应关系
def index(request):
    # 进行处理，和M和T进行交互。。。
    return HttpResponse('老铁，没毛病！')

def index2(request):
    return HttpResponse('Hello,Python!')
