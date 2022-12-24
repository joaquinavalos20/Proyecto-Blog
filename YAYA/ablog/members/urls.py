from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView
from django.contrib.auth import views as auth_views
from . import views 
#from . import views
urlpatterns = [
    path("register/", UserRegisterView.as_view(), name="register"),
    path("editprofile/", UserEditView.as_view(), name="editprofile"),
    #path("password/", auth_views.PasswordChangeView.as_view(template_name="registration/changepass.html"))
    path("password/", PasswordsChangeView.as_view(template_name="registration/changepass.html")),
    path("passwordsuccess/", views.passwordsuccess, name="passwordsuccess"),
]