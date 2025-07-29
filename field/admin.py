from django.contrib import admin

# Register your models here.
from .models import Cost, Cultivation_calender, Field, Image, Job, Note, Product, Voice

admin.site.register(Cost)
admin.site.register(Cultivation_calender)
admin.site.register(Field)
admin.site.register(Image)
admin.site.register(Job)
admin.site.register(Note)
admin.site.register(Product)
admin.site.register(Voice)
