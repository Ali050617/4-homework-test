from django.contrib import admin
from  .models import Authors


@admin.register(Authors)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'bio', 'birth_date', 'nationality')
    search_fields = ('first_name', 'last_name', 'bio', 'nationality')
    list_filter = ('birth_date', )