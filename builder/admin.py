from django.contrib import admin
from .models import Mockup, Dress


# Register your models here.
@admin.register(Mockup)
class MockupAdmin(admin.ModelAdmin):
    pass


@admin.register(Dress)
class DressAdmin(admin.ModelAdmin):
    pass
