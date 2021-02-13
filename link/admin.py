from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm


class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = User
        fields = "__all__"


class MyUserAdmin(UserAdmin):

    form = MyUserChangeForm

    fieldsets = UserAdmin.fieldsets


admin.site.register(User, MyUserAdmin)