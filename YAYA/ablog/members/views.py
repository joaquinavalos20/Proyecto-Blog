from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PassChangeForm



class PasswordsChangeView(PasswordChangeView):
    #form_class = PasswordChangeForm
    form_class = PassChangeForm
    success_url = reverse_lazy("passwordsuccess")
    #success_url = reverse_lazy("home")

def passwordsuccess(request):
    return render(request, "registration/passwordsuccess.html")

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("login")


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/editprofile.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user