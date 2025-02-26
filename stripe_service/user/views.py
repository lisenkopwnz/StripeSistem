from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView

from user.forms import CustomUserCreationForm


class RegisterView(FormView):
    template_name = "user/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("user:login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = "user/login.html"
    authentication_form = AuthenticationForm

    def get_success_url(self):
        return reverse_lazy("items:item_list")


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("items:item_list")
