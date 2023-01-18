from django.shortcuts import render,HttpResponse


# Create your views here.
def hello_world(request):
    return render(request, "app1/hello_world.html")

def welcome(request):
    return HttpResponse("<p> welcome to httprespose </p>")