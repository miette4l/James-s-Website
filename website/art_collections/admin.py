from django.contrib import admin
from art_collections.models import Collection, Work


# Register your models here.
class CollectionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Collection, CollectionAdmin)


class WorkAdmin(admin.ModelAdmin):
    pass


admin.site.register(Work, WorkAdmin)