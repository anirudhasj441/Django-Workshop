from django.contrib import admin
from my_portfolio_app.models import ClasFormModel
# Register your models here.
class ClasFormAdmin(admin.ModelAdmin):
    search_fields = ["pk","full_name"]
    list_filter = ["full_name"]
    list_display = [
        "pk",
        "created_at",
        "full_name",
        "email_id",
        "contact_number",
        "message",
    ]
    list_editable = ["full_name"]

admin.site.register(ClasFormModel,ClasFormAdmin)
admin.site.site_header = "My Portfollio"
admin.site.site_index = "My Portfollio"
admin.site.index_title = "My Portfollio"