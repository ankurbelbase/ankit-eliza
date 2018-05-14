from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from classroom.forms import TeacherSignUpForm


from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy



from classroom.decorators import teacher_required
from django.contrib.auth.models import User




class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return user