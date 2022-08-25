from django.contrib import admin
from .models import Standard,Author,Standard_to_Author

admin.site.register(Standard)
admin.site.register(Author)
admin.site.register(Standard_to_Author)
# Register your models here.
