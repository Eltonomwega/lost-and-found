from django.contrib import admin
from .models import Post
from django.contrib.auth.admin import UserAdmin
from .models import Claim

# Register your models here.



#displaying specific fields in the admin site and adding a search option

class PostCustom(admin.ModelAdmin):
    list_display = ['title','description','category','location','image','When','claimed']
    search_fields = ['title','category','When','location']

class ClaimAdmin(admin.ModelAdmin):
    list_display = ['item_claimed','claimed_by','date_claimed','accepted']
    search_fields = ['item_claimed','claimed_by','date_claimed','accepted']

    list_filter = ('date_claimed',)
    fieldsets = ()
    ordering = ('-date_claimed',)
    filter_horizontal = ()

admin.site.register(Post, PostCustom)
admin.site.register(Claim, ClaimAdmin)
