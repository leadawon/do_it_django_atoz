from django.shortcuts import render

# Create your views here.
def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )
#blog\views.py 처럼 딕셔너리로 post를 받을 필요가 없다.

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html'
    )