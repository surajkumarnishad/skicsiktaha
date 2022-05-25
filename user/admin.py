from django.contrib import admin

# Register your models here.
from .models import *


class contactAdmin(admin.ModelAdmin):
    list_display=('name','email','mobile','message')


admin.site.register(contact,contactAdmin)



class galleryAdmin(admin.ModelAdmin):
    list_display=('id','pdes','gpic','gdate')

admin.site.register(gallery,galleryAdmin)


class notificationAdmin(admin.ModelAdmin):
    list_display=('name','rpic','rdate')

admin.site.register(notification,notificationAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display=('cname','cpic','cdate')

admin.site.register(category,categoryAdmin)


class coursesAdmin(admin.ModelAdmin):
    list_display = ('cname', 'cpic', 'cdate')

admin.site.register(courses,coursesAdmin)


class admissionAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'pcourse', 'branch','cmpname','cmplogo','city','pyear','designation','stupic','pdate')

admin.site.register(admission,admissionAdmin)

class facultyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','about')
admin.site.register(faculty,facultyAdmin)






