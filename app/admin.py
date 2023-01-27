from django.contrib import admin

from .models import Question, Person, Choice, Author, Blog, Entry

admin.site.register(Question)
admin.site.register(Person)
admin.site.register(Choice)
admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Entry)
