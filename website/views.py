
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')


def skills(request):
    return render(request, 'skills.html')


def projects(request):
    return render(request, 'projects.html')


def photography(request):
    return render(request, 'photography.html')


def about(request):
    from datetime import date

    start = date(2019, 8, 29)
    end = date(2022, 6, 10)
    total_time = (end - start).days
    time_left_today = (end - date.today()).days

    percent_engineer = 100 - int(time_left_today / total_time * 100)


    return render(request, 'about.html', {'days_until_graduation': time_left_today,
                                          'percent_engineer': percent_engineer})


def contact(request):
    return render(request, 'contact.html')


def skills(request):
    return render(request, 'skills.html')


def skills(request):
    return render(request, 'skills.html')
