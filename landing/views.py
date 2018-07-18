from django.shortcuts import render

# Create your views here.


def index(request):
    css_files = ['css/testing.css','css/landing.css']
    
    my_dict = {'title': 'Code Solutions', 'css': css_files}

    return render(request,'landing/index.html', context = my_dict)


