from django.contrib import admin
from . models import AboutMe, Skills, Projects, Rezume


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'client', 'project_date', 'project_url', 'created_date', 'view_portfolio_numbers')
    list_display_links = ('name', 'project_url',)
    list_editable = ('view_portfolio_numbers', )


class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'city', 'birthday', 'degree', 'phone_number')
    list_editable = ('degree', 'phone_number')


class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level_of_knowledge')
    list_editable = ('level_of_knowledge', )


class RezumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'edu_or_job', 'title', 'date', 'name')


admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Projects, ProjectAdmin)
admin.site.register(Rezume, RezumeAdmin)

