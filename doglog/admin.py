from django.contrib import admin
from doglog.models import Person, Shift, Availability, Holiday

# Register your models here.

#admin permission to
class PersonAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name:',       {'fields': ['first_name','last_name']}),
        ('Meces username', {'fields': ['mcecs_username']}),
        ('PDX username', {'fields': ['pdx_username']}),
        ('CAT username', {'fields': ['cat_username']}),
        ('CAT handle', {'fields': ['cat_handle']}),
        ('Email', {'fields': ['preferred_email']}),
        ('# of missed meetings', {'fields': ['number_of_missed_mettings']}),
        ('# of no call/no show meetings', {'fields':['number_of_no_call']}),
        ('# of strikes', {'fields':['strikes']}),
        ('Availability flag', {'fields': ['availability_flag']}),
        ('Active Dog', {'fields': ['dog_flag']}),
        ('Dedog', {'fields': ['dedog_flag']}),
        ('Archived Dog',  {'fields': ['archived_dog_flag']}),
        ('Alternative Dog', {'fields': ['alt_dog_flag']}),
        ('Note',{'fields':['notes']}),
        ('# of absent hours', {'fields':['num_of_absent_hr']}),
        ('# of made-up hours', {'fields':['num_of_made_up_hr']}),
        ('# of no call/no show hours', {'fields':['num_of_no_call_hr']}),



    ]

    list_display = ('first_name', 'last_name', 'cat_username', 'cat_handle',
                    'preferred_email', 'notes')
    search_fields = ['first_name', 'last_name', 'cat_username','cat_handle']

class ShiftAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Start date and time', {'fields': ['start_date_and_time']}),
        ('End date and time', {'fields': ['end_date_and_time']}),
        ('Expiry Date', {'fields' : ['expiry_date']}),
        ('Dropped Flag', {'fields' : ['dropped_flag']}),
        ('Missed Flag', {'fields' : ['missed_flag']}),
    ]


    list_display = ('start_date_and_time', 'end_date_and_time', 'dropped_flag',
               'missed_flag' )



class AvailabilityAdmin(admin.ModelAdmin):
    fieldsets = [

        ('Start date and time', {'fields': ['start_date_and_time']}),
        ('End date and time', {'fields': ['end_date_and_time']}),
        ('Effective Date', {'fields' : ['effective_date']}),
    ]


    list_display = ('start_date_and_time', 'end_date_and_time', 'effective_date' )


class HolidayAdmin(admin.ModelAdmin):

    fieldsets = [
        ( "Name", {'fields' : ['name']}),
        ("Date",{'fields' : ['date']}),
    ]

    list_display=('name','date')


admin.site.register(Holiday,HolidayAdmin)
admin.site.register(Shift, ShiftAdmin)
admin.site.register(Availability,AvailabilityAdmin)

admin.site.register(Person, PersonAdmin)
