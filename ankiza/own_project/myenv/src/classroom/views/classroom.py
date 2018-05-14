from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = 'signup.html'


def home(request):
    # if request.user.is_authenticated:
    return render(request, 'home.html')
