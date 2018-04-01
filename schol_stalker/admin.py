from django.contrib import admin

from school_stalker.models import Book


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(Book, BookAdmin)
