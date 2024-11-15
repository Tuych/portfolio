from django.shortcuts import render, redirect
from .models import AboutMe, Skills, Projects, Rezume
from django.shortcuts import get_object_or_404
from .forms import ContactForm
from django.core.mail import EmailMessage


def index(request):
    my_info = get_object_or_404(AboutMe)
    skills = Skills.objects.all()
    projects = Projects.objects.all()
    rezume = Rezume.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            EmailMessage(
                ' {}, from {}'.format(subject, name), message,
                '{}'.format(email),
                ['myportfoliomessages05@gmail.com'],
                [],
                reply_to=[email]
            ).send()
            return redirect('success')
        else:
            return redirect('index')
    else:
        form = ContactForm
    context = {
        'info': my_info,
        'skills': skills,
        'projects': projects,
        'form': form,
        'navbar_section': True,
        'rezume': rezume,

    }
    return render(request, 'main/index.html', context)


def portfolio_detail(request, pk):
    project = get_object_or_404(Projects, id=pk)
    context = {
        'project': project
    }
    return render(request, 'main/portfolio-details.html', context)


def success(request):
    return render(request, 'main/success.html')


def custom_404(request, exception):
    return render(request, 'main/404.html', status=404)
