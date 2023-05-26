from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "index.html")
def clothes(request):
    return render(request, "clothes.html")
def bags(request):
    return render(request, "bags.html")
def accessories(request):
    return render(request, "accessories.html")
def shoes(request):
    return render(request, "shoes.html")
def books(request):
    return render(request, "books.html")