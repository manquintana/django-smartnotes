from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
#from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView



from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

''' CLASS-BASED VIEWS: Con esto nos ahorramos definir la view como antes'''
from django.views.generic import TemplateView
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today':datetime.today()}
# Esto ya no es necesario
# def home(request):
#     #return HttpResponse('Hello,world!')
#     return render(request, 'home/welcome.html', {'today':datetime.today()})

'''Voy a hacer lo mismo para la otra funcion que definia una view, ahora será una Class-based view'''
# @login_required(login_url='/admin') #si esta logueado, muestra authorized, sino redirige a /admin
# def authorized(request):
#     return render(request, 'home/authorized.html', {})
class Authorizedview(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'


