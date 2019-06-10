import sweetify
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string


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


def introduccion_ds(request):
    if request.method == 'POST':
        _submit_form(request)

    return render(request, 'landing/index-ds.html')


def python_crash_course(request):
    if request.method == 'POST':
        _submit_form(request)

    return render(request, 'landing/index.html')
