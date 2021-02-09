from django.shortcuts import render

# Create your views here.

def responsivedesign(request):
    context = {}
    return render(request,'designapp/responsivedesign.html',context)