from django.contrib import admin
from .models import Messages, Depatrments, Doctorlist, Appointment
# Register your models here.

@admin.register(Messages)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'message')
    
@admin.register(Depatrments)
class AddDepatrments(admin.ModelAdmin):
    list_display = ('id', 'dep_name', 'description') 

@admin.register(Doctorlist)
class Doctorslist(admin.ModelAdmin):
    list_display = ('id', 'doc_name', 'doc_spec', 'doc_dep', 'img')
    
@admin.register(Appointment)
class Appointment(admin.ModelAdmin):
    list_display= ('id', 'name', 'mail', 'mobile', 'doctor', 'date', 'booked_on' )