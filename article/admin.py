from django.contrib import admin
from .models import ToolsAndInnovations, Startdata, Metadata, Recommendations
# Register your models here.

class ToolsAndInnovationAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ToolsAndInnovations._meta.get_fields()]
admin.site.register(ToolsAndInnovations, ToolsAndInnovationAdmin)


class StartdataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Startdata._meta.get_fields()]
admin.site.register(Startdata, StartdataAdmin)


class MetadataAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Metadata._meta.get_fields()]
admin.site.register(Metadata, MetadataAdmin)


class RecommendationsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Recommendations._meta.get_fields()]
admin.site.register(Recommendations, RecommendationsAdmin)
