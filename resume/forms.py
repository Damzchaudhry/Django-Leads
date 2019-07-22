from django import forms
from .models import Resume,Upload_resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ["school_inter",
        "board_inter",
        "year_inter",
        "inter",
        "add", 
        "phone",
        "school_high",
        "year_high",
        "high",
        "board_high",
     
        "email",
        "skill",
        "area_of_skill",
        "hob",
        "gender",
        "dob",
        "exp",
        "ug",
        "ug_coll",
        "year_ug",


        ]
class UploadForm(forms.ModelForm):
    class Meta:
        model = Upload_resume
        fields =["resume"]

            
        