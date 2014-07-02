from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    # Tweak the Poll admin page
    # fields = ['pub_date', 'question']
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    # Tweak the "change list" page
    list_display = ('question', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question']
    # Change lists give you free pagination.
    # The default is to display 100 items per page.
    date_hierarchy = 'pub_date'

admin.site.register(Poll, PollAdmin)

