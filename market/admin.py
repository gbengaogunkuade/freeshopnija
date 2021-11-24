from django.contrib import admin
from market.models import MarketPostCategory, SellerMarketPost





# ADMIN CONSOLE PAGE SETUP
# ========================================================================
# USE "LIST_DISPLAY" TO DISPLAY THE MODEL FIELDS IN THE ADMIN CONSOLE
# USE "PREPOPULATED_FIELDS" TO AUTOMATE THE SLUG PROCESS IN THE ADMIN CONSOLE
class MarketPostCategoryAdmin(admin.ModelAdmin):
    list_display = ['category', 'description']
    # list_editable = ['description']  # EDITING FROM THE ADMIN CONSOLE
    # prepopulated_fields = {'slug': ('title',)}



# ADMIN CONSOLE PAGE SETUP
# ========================================================================
# USE "LIST_DISPLAY" TO DISPLAY THE MODEL FIELDS IN THE ADMIN CONSOLE
# USE "PREPOPULATED_FIELDS" TO AUTOMATE THE SLUG PROCESS IN THE ADMIN CONSOLE
class SellerMarketPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'seller', 'sellcategory', 'price']
    list_display_links = ['title']
    list_editable = ['seller', 'sellcategory']     # EDITING FROM THE ADMIN CONSOLE
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title']       # SEARCH FIELD FOR SEARCHING FOR "title" IN THE ADMIN CONSOLE
    list_filter = ['seller', 'sellcategory']       # FILTER FOR "title" and "sellcategory" IN THE ADMIN CONSOLE
    # date_hierarchy = 'date_posted'      # DATE HIERARCHY
    # readonly_fields = ['date_posted']     # READ ONLY FIELD




# Register your models here.
admin.site.register(MarketPostCategory, MarketPostCategoryAdmin)
admin.site.register(SellerMarketPost, SellerMarketPostAdmin)

