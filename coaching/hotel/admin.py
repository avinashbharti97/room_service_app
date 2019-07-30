from django.contrib import admin
from .models import Asset, Worker, Task, AllocateTask

# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    pass

admin.site.register(Asset)
admin.site.register(Worker)
admin.site.register(Task)
admin.site.register(AllocateTask)