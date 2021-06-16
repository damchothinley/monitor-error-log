from ErrorLog.settings import EMAIL_HOST, EMAIL_HOST_USER
from django.http import HttpResponse  # newly added
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def HomePageView(request):
    return HttpResponse("Hello World!")


def ErrorView(request):
    return ("<em>Email send successfully</em>")
