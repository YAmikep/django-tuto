from polls.models import Poll, Choice
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
        #('Date information', {'fields': ['pub_date']}),
    ]
    #fields = ['pub_date', 'question']
    
admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
#admin.site.register(Poll)