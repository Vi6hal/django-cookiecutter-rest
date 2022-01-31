from accounts.models import User

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, UsernameField
from django.utils.translation import gettext_lazy as _


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = "__all__"
        field_classes = {"username": UsernameField}


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (
            None,
            {"fields": ("email", "password", "first_name", "last_name")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = (
        "email",
        "is_staff",
        "is_active",
    )
