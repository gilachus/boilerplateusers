from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from .forms import PerfilUsuarioCreateForm
from django.urls import reverse_lazy


class SignupView(generic.CreateView):
    # model = User
    template_name = "registration/signup.html"
    # form_class = UserCreationForm
    form_class = PerfilUsuarioCreateForm
    success_url = reverse_lazy('login')

# ↓ ignoren
class ClassView(View):
    pass

def success(request):
    """funcion vista"""
    if request.method == 'GET':
        return HttpResponse('result')

@method_decorator(login_required, name='dispatch')
class GreetingView(View):
    """clase vista retornando string"""
    greeting = "Good Day"
    def get(self, request):
        return HttpResponse(self.greeting)

class MyFormView(View):
    """clase vista para forms"""
    # form_class = MyForm
    # initial = {'key': 'value'}
    # template_name = 'form_template.html'

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(initial=self.initial)
    #     return render(request, self.template_name, {'form': form})

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/success/')

    #     return render(request, self.template_name, {'form': form})