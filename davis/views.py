from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.http import FileResponse, Http404
from .models import Resume
import os



# Create your views here.
def index(request):
    user = CustomUser.objects.all()
    about = About.objects.all()
    skill = Skill.objects.all()
    resume = Education.objects.all()
    certi = Certificate.objects.all()
    experi = Experience.objects.all()
    port = Portfolio.objects.all()
    portcate = PortfolioCategory.objects.all()
    services = Services.objects.all()
    testimonial = Testimonial.objects.all()


    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_text = request.POST.get('message')

        try:
            send_mail(
                subject,
                f"Message from {name} ({email}):\n\n{message_text}",
                'davidogheneothuke42@gmail.com',
                ['davidogheneothuke42@gmail.com'],
            )
            messages.success(request, 'Email sent successfully!')
        except Exception as e:
            messages.error(request, f"Failed to send email: {e}")

    context = {
        'user':user,
        'about':about,
        'skill':skill,
        'resume':resume,
        'certi':certi,
        'experi':experi,
        'port':port,
        'portcate':portcate,
        'services':services,
        'testimonial':testimonial,
        'show_sidebar':True,
    }
    return render(request, 'index.html', context)


def portfolio_details(request, pk):
    portfolio_detail = Portfolio.objects.get(id=pk) 

    context = {
        'portfolio_detail':portfolio_detail,
        'show_sidebar':False,
    }

    return render(request, 'portfolio-details.html', context)


def services_details(request, po):
    services_detail = Services.objects.get(id=po)
    bullet = ServiceBullet.objects.filter(service=services_detail).order_by('order')

    context = {
        'services_detail':services_detail,
        'bullet':bullet,
        'show_sidebar':False,
    }

    return render(request, 'service-details.html', context)


def services(request):
    servic = Services.objects.all()

    context = {
        'servic':servic,
        'show_sidebar':False,
    }
    return render(request, 'services.html', context)


def form(request):
    if request.method == 'POST':
        picture = request.FILES.get('picture')
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        details = request.POST.get('details')

        Testimonial.objects.create(
            picture=picture,
            name=name,
            subject=subject,
            details=details,
        )

        messages.success(request, 'Testimonial Sent Successfully')

    return render(request, 'form.html', {"show_sidebar": False})


def download_resume(request):
    try:
        resume = Resume.objects.latest("updated_at")
        file_path = resume.file.path

        if os.path.exists(file_path):
            return FileResponse(
                open(file_path, "rb"),
                as_attachment=True,
                filename=os.path.basename(file_path),
            )
        else:
            raise Http404
    except Resume.DoesNotExist:
        raise Http404("Resume not found")
