from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegistrationForm, UserAdminCreationForm, UserAdminChangeForm
from .models import Stratizen

# Register your models here.

class CustomUserAdmin(UserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ['registration_no','email','is_active','is_admin','is_staff','last_login','date_joined']
    search_fields = ['registration_no', 'email']

    add_fieldsets = [
        [None, {
            'classes': ('wide',),
            'fields': ('registration_no','email','password1','password2')}
        ],
    ]

    list_filter = ('is_admin',)
    fieldsets = ()
    ordering = ('registration_no',)
    filter_horizontal = ()


    

admin.site.register(Stratizen, CustomUserAdmin)
