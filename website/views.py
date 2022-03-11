from datetime import date
from dateutil.relativedelta import relativedelta

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from .forms import ContactForm

from .mail import MailMan

def the_website(request):
    return render(request, 'website.html', {'current_year': date.today().year})

def home(request):
    return render(request, 'home.html', {'current_year': date.today().year})

def about(request):
    # Calculate time left until graduation and how much of the bachelors is completed.
    start = date(2019, 8, 29)
    end = date(2023, 1, 1)
    total_time = (end - start).days
    time_left_today = (end - date.today()).days
    percent_engineer = 100 - int(time_left_today / total_time * 100)

    # Calculate age
    birthdate = date(1996, 2, 10)
    age = relativedelta(date.today(), birthdate).years

    return render(request, 'about.html', {'days_until_graduation': time_left_today,
                                          'percent_engineer': percent_engineer,
                                          'age': age,
                                          'current_year': date.today().year})

def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = f'Sender name: {form.cleaned_data["name"]}\n'\
                      f'Sender mail: {form.cleaned_data.get("mail", "Not given")}\n\n'\
                      f'Message: {form.cleaned_data["message"]}\n\n'

            MailMan.send_mail(settings.MAIL['username'], settings.MAIL['password'],
                              settings.MAIL['recipient'], message, subject='Website contact')
        return HttpResponseRedirect('/contact')

    else:
        return render(request, 'contact.html', {'form': ContactForm(),
                                                'current_year': date.today().year})
