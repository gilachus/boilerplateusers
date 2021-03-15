from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import PerfilUsuarioCreateForm, PerfilUsuarioChangeForm
from .models import PerfilUsuario


class PerfilUsuarioAdmin(UserAdmin):
    add_form = PerfilUsuarioCreateForm
    form = PerfilUsuarioChangeForm
    model = PerfilUsuario
    list_display = ['username', 'email', 'first_name', 'last_name', 'edad', 'is_staff']
    UserAdmin.fieldsets[1][1]['fields'] = ('first_name', 'last_name', 'email','edad')
    # fieldsets = UserAdmin.fieldsets + (
    #     (None, {'fields': ('edad',)}),
    # )
    UserAdmin.add_fieldsets[0][1]['fields'] = UserAdmin.add_fieldsets[0][1]['fields'] + ('edad',)
    # add_fieldsets = UserAdmin.add_fieldsets + (
    #     (None, {'fields': ('edad',)}),
    # )

admin.site.register(PerfilUsuario, PerfilUsuarioAdmin)
