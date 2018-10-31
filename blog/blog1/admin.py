from django.contrib import admin
from blog1.models import *

# Register your models here.
admin.site.register(article)
admin.site.register(comment)
admin.site.register(User)
