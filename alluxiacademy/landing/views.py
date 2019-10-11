import sweetify
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string
from .models import Course
from django.conf import settings
import pdb
import requests

def send_mail_wrapper(title, template, context, recipients):
    html_message = render_to_string(
        template, context)
    send_mail(title,
              html_message,
              '',
              recipients,
              html_message=html_message,
              fail_silently=False)


def _submit_form(request):
    try:
        email = request.POST.get('email')
        content = request.POST.get('content')

        context = {
            'email': email,
            'content': content,
        }
        send_mail_wrapper('Contacto Alluxi Academy',
                          'landing/contact_email.html',
                          context, ['hola@alluxi.mx'])

        sweetify.success(request, '¡Gracias por tu mensaje! Nos pondremos en contacto contigo a la brevedad.')
    except Exception as e:
        sweetify.error(request, 'Error: ' + str(e))


def introduccion_dg(request):
    if request.method == 'POST':
        _submit_form(request)

    return render(request, 'landing/index-dg.html')


def introduccion_ds(request):
    if request.method == 'POST':
        _submit_form(request)

    return render(request, 'landing/index-ds.html')


def python_crash_course(request):
    if request.method == 'POST':
        _submit_form(request)

    return render(request, 'landing/index-py.html')

def image_url_fixed(url_to_check, request):
    url_fixed = "https://via.placeholder.com/150"

    if (url_to_check == "" or url_to_check == None):
        return url_fixed

    domain = request.build_absolute_uri('/')[:-1]    
    response = requests.get(domain+url_to_check)

    if (response.status_code == 200):
        return url_to_check 
    return url_fixed

def get_course(request, slug = ""):
    if request.method == 'POST':
        _submit_form(request)

    if slug == "":
        course = Course.objects.get(featured=True)
    else:
        course = Course.objects.get(slug=slug)

    courses = Course.objects.all().order_by('-id')[:3]
    image_url  = image_url_fixed(course.instructor.photo.url, request)
    context = {'course': course, 'courses': courses, 'image_url_fixed': image_url}
          
    return render(request, 'landing/index-course.html', context)

