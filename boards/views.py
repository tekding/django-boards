
from django.http import HttpResponse
from django.shortcuts import render
from .models import Board

def home(request):
        boards = Board.objects.all()
        # boards_names = list()
        # for board in boards:
        #         boards_names.append(board.name)        
        # boards_names =[board.name for board in boards]
        # response_html = '<br>'.join(boards_names)
        # return HttpResponse (response_html)
        return render(request,'home.html',{'boards':boards})
def index(request):
        return render(request,'index.html')
# Create your views here.
