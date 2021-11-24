from django.contrib import admin
from visitor.models import UserProfile





# ADMIN CONSOLE PAGE SETUP
# ========================================================================
# USE "LIST_DISPLAY" TO DISPLAY THE MODEL FIELDS IN THE ADMIN CONSOLE
# USE "PREPOPULATED_FIELDS" TO AUTOMATE THE SLUG PROCESS IN THE ADMIN CONSOLE
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'company_name', 'telephone_number']
    # prepopulated_fields = {'slug': ('title',)}
    # search_fields = ['company_name']




# Register your models here.
admin.site.register(UserProfile, UserProfileAdmin)




