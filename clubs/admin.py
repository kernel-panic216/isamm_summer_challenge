from django.contrib import admin
from .models import President,Etudiant,Club,SuperAdmin1,SuperAdmin2,UserProfile,Activity,demander, Event, notification

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'niveau', 'skills', 'site', 'tel')

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(UserProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-niveau', 'user')
        return queryset

    user_info.short_description = 'Info'


admin.site.register(UserProfile)
admin.site.register(demander)
 
admin.site.register(notification)
admin.site.register(Club)
admin.site.register(Activity)
admin.site.register(Event)
# Register your models here.
