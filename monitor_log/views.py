from ErrorLog.settings import EMAIL_HOST, EMAIL_HOST_USER
from django.http import HttpResponse  # newly added
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


def HomePageView(request):
    return HttpResponse("Hello World!")


def ErrorView(request):
    try:
        print("%s" % (EMAIL_HOST_USER))
        subject = "test"
        message = "mailing trial"
        from_email = EMAIL_HOST_USER
        send_mail(subject, message, from_email, [
            from_email], fail_silently=True)
    except Exception:
        return Exception
    else:
        return ("<em>Email send successfully</em>")
