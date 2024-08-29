from django.contrib import admin
from .models import PersonalInformation, About, Projects, Skills, Achievements, Contact


class PersonalInformationAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
    )
    search_fields = ["name"]


admin.site.register(PersonalInformation, PersonalInformationAdmin)
admin.site.register(About)
admin.site.register(Projects)
admin.site.register(Skills)
admin.site.register(Achievements)
admin.site.register(Contact)
