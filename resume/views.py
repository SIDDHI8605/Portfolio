from django.shortcuts import render,redirect

from django.core.mail import send_mail
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from .forms import ContactForm
from django.conf import settings
# from django.http import FileResponse, Http404
# import os

# Create your views here.
def home(request):
  return render(request,"home.html")
def about(request):
  return render(request,"about.html")
def projects(request):
  projects_show=[
    {"title":"Garage Management System",
    'path':'image/garage.jpg'
  
    },
    {"title":"Attendance Management System",
    'path':'image/attendance.png'
    },
    {"title":"Tic Tac Toe",
    'path':'image/game.png'
    },
  
    {"title":"Portfoio",
    'path':'image/portfolio.png'
    },
   
  ]
  return render(request,"projects.html",{'projects_show':projects_show})

def certificate(request):
  return render(request,"certificate.html")

# def contact(request):
#    if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         contact_number = request.POST.get('contact')

#         Contact.objects.create(
#             name=name,
#             email=email,
#             password=password,
#             contact_number=contact_number
#         )
#         return redirect('success')  # After submit, go to success page

#   return render(request, "contact.html")
#   # return render(request,"contact.html")

# def success(request):
#     return render(request, "success.html")

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Email to site owner (you)
            subject = f'New Contact Form Submission from {name}'
            body = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
            send_mail(subject, body, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])

            # Thank-you email to visitor
            thank_you_subject = 'Thank You for Contacting Us'
            thank_you_message = f'Hi {name},\n\nThank you for reaching out to Me. I have received your message'
            send_mail(thank_you_subject, thank_you_message, settings.EMAIL_HOST_USER, [email])

            return redirect('thank_you')  # Optional: redirect to a thank-you page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})



def thank_you_view(request):
    return render(request, 'thank_you.html')


def success(request):
    return render(request, "success.html")


def resume(request):
  resume_path = "myapp/resume.pdf"
  resume_path = staticfiles_storage.path(resume_path)

  if staticfiles_storage.exists(resume_path):
    with open(resume_path,"rb") as resume_file:
      response=HttpResponse(resume_file.read(),content_type="application/pdf")
      response['Content-Disposition']='attachment'; filename="resume.pdf"
      return response
  else:
    return HttpResponse("resume not found",status=404)


# def download_resume(request):
#     file_path = os.path.join('static', 'myapp', 'resume.pdf')  # adjust if needed
#     if os.path.exists(file_path):
#         return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='Siddhi_Mahajan_Resume.pdf')
#     else:
#         raise Http404("Resume not found")

