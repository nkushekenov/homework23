from django.shortcuts import render


def home(request):
    return render(request, 'HW23/base.html')




def custom_page(request):
    return render(request, 'HW23/child_template.html')
