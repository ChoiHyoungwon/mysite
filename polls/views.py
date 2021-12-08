from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index. 안녕하세요 폴스 인덱스에 오신것을 환영합니다." )