from django.contrib import admin
from .models import *
# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
	pass

class OrderAdmin(admin.ModelAdmin):
	pass

class MerchantAdmin(admin.ModelAdmin):
	pass

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Merchant,MerchantAdmin)
admin.site.register(Order,OrderAdmin)
