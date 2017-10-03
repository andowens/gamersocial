from django.contrib import admin
from . import models


class GroupMemberInline(admin.TabularInline):
    models = models.GroupMember

admin.site.register(models.Group)


