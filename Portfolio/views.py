from django.shortcuts import render
from .models import Project, Skill, Tool

def portfolio_view(request):
    projects = Project.objects.all()
    skills = Skill.objects.all()
    tools = Tool.objects.all()
    context = {
        'projects': projects,
        'skills': skills,
        'tools': tools
    }
    return render(request, 'portfolio/portfolio.html', context)



from django.http import HttpResponse

def om(request):
    domain_owner = 'HexaCore by Om Gajipara'
    return HttpResponse(f"This domain is under: {domain_owner}")










#email


from django.shortcuts import render, redirect
from django.core.mail import send_mail, EmailMessage, get_connection
from django.conf import settings
from django.contrib import messages
from .models import Contact  # Ensure you have imported your Contact model

def contact(request):
    if request.method == 'POST':
        fname = request.POST.get("name")
        femail = request.POST.get("email")
        phone = request.POST.get("phone")
        desc = request.POST.get("desc")
        query = Contact(name=fname, email=femail, phoneNumber=phone, description=desc)
        query.save()

        # email sending logic
        from_email = settings.EMAIL_HOST_USER
        connection = get_connection()
        connection.open()
        email_message = EmailMessage(
subject=f'Email response from HexaCore ',
body=f"""
Dear {fname},

We have received your response. Here are the details you provided:

Your Email: {femail}
Your Phone Number: {phone}
Description:{desc}

We will get back to you as soon as possible.
Best regards,
Hexacore Team
Visit our website:- omgajipara.pythonanywhere.com

Thanks for visiting our Email Web Application by HexaCore

Om Gajipara
            """,
            from_email=from_email,
            to=[femail, 'hexacore.business@gmail.com'],
            connection=connection
        )

        connection.send_messages([email_message])
        connection.close()

        messages.info(request, "Thanks for reaching us")
        return redirect('contact_success')  # Redirect to the same contact page after form submission

    return render(request, 'emailapp/contact.html')



def contact_success(request):
    return render(request,'emailapp/contact_success.html')
