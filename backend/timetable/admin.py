from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import TimeTable, Period


# Register your models here.
@admin.register(TimeTable)
class TimeTableAdmin(ImportExportModelAdmin):
    list_display = [ "subject" ]
    search_fields = [ "subject" ]
    filter_horizontal = [ "periods" ]


@admin.register(Period)
class PeriodAdmin(ImportExportModelAdmin):
    list_display = ("start", "end", "day")
    list_filter = ("start", "end", "day")
