from django.contrib import admin
from . import models

# Register your models here.
class AdminOffersWorks(admin.ModelAdmin):
    list_display = ['name', 'old_prize', 'new_prize', 'image', 'date']
admin.site.register(models.OfferWorks,AdminOffersWorks)

class AdminHappyClients(admin.ModelAdmin):
    list_display = ['client_name_last', 'client_position', 'client_image', 'client_date']
admin.site.register(models.HappyClients, AdminHappyClients)

class AdminResentBlog(admin.ModelAdmin):
    list_display = ['short_text', 'author', 'blog_image']
admin.site.register(models.ResentBlog, AdminResentBlog)

class AdminAgents(admin.ModelAdmin):
    list_display = ['agent_name', 'agent_img', 'date']
admin.site.register(models.Agents, AdminAgents)

class AdminContact(admin.ModelAdmin):
    list_display = ['id' ,'name', 'date', 'subject']
    ordering = ('name', 'date', 'subject')
admin.site.register(models.Contact, AdminContact)

