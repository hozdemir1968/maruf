from django.shortcuts import render

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        context={
            'isim':request.user.username,
        }
    else:
        context={
            'isim':'Misafir',
        }
    return render(request,'home/home.html',context)
    