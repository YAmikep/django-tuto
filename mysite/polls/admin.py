from polls.models import Poll, Choice
from django.contrib import admin

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        #('Date information', {'fields': ['pub_date']}),
    ]
    #fields = ['pub_date', 'question']
    inlines = [ChoiceInline]
    
admin.site.register(Poll, PollAdmin)
#admin.site.register(Choice)
#admin.site.register(Poll)