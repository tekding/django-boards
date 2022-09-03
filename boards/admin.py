from django.contrib import admin
from .models import Standard,Author,Standard_to_Author,Standard_to_Company,Company

admin.site.register(Standard)
admin.site.register(Author)
admin.site.register(Company)
admin.site.register(Standard_to_Author)
admin.site.register(Standard_to_Company)
# Register your models here.
