from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import models
from .models import PerfilUsuario


class PerfilUsuarioCreateForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = PerfilUsuario
        fields = UserCreationForm.Meta.fields + ('edad',)

class PerfilUsuarioChangeForm(UserChangeForm):
    class Meta:
        model = PerfilUsuario
        fields = UserChangeForm.Meta.fields