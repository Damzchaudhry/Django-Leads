from django.contrib import admin

from .models import Resume,Upload_resume

from import_export.admin import ImportExportModelAdmin
@admin.register(Upload_resume)
class Resumeb(admin.ModelAdmin):
	list_display=["author","Upload_date","id"]
	list_filter=["Upload_date"]
	class Meta:
		model =Upload_resume
			
		


@admin.register(Resume)

class ResumeA(ImportExportModelAdmin):

    list_display = ["author","created_date","id"]


    list_filter = ["created_date"]
    class Meta:
        model = Resume

