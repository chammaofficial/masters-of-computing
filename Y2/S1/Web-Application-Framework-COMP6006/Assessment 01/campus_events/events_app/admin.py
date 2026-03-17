from django.contrib import admin
from django.utils import timezone

from events_app.models import Category, Event

# Register your models here.
@admin.action(description = 'Approve Selected Events')
def approve_selected_events(modeladmin, request, queryset):
    queryset.update(is_approved=True, approved_at=timezone.now())

@admin.action(description = 'Reject Selected Events')
def reject_selected_events(modeladmin, request, queryset):
    queryset.update(is_approved=False, approved_at=None)

class EventAdmin(admin.ModelAdmin):
    actions = [approve_selected_events, reject_selected_events]
    list_display = ['title','description','category','location','start_datetime','end_datetime','is_approved']
    list_filter = ['is_approved', 'category']
    search_fields = ['category__name']

admin.site.register(Category)
admin.site.register(Event, EventAdmin)