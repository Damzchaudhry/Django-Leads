from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Resume(models.Model):
	author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "author ")

	# -----------------------------------------Persnol Detail---------------------------------------
	phone = models.CharField(max_length = 50,verbose_name = "phone")
	email =models.CharField(max_length=25,verbose_name="email")
	hob=models.CharField(max_length=250,verbose_name="hob")
	gender=models.CharField(max_length=15,verbose_name="gender")
	dob= models.DateTimeField(auto_now_add=False,verbose_name="dob")
	add = models.CharField(max_length=250, verbose_name="add")

	school_inter =models.CharField(max_length=100,verbose_name="school_inter")
	inter = models.CharField(max_length=25,verbose_name="inter")
	board_inter=models.CharField(max_length=25,verbose_name="board_inter")
	year_inter=models.DateTimeField(auto_now_add=False,verbose_name="year_inter")
	# ----------------------------------------------10th-----------------------

	high =models.CharField(max_length=25,verbose_name="high")
	school_high =models.CharField(max_length=100,verbose_name="school_high")
	board_high=models.CharField(max_length=25,verbose_name="board_high")
	year_high=models.DateTimeField(auto_now_add=False,verbose_name="year_high")
	# ---------------------------------------Graduation--------------------------


	ug =models.CharField(max_length=15,verbose_name="ug")
	ug_coll=models.CharField(max_length=50,verbose_name="ug_coll")
	year_ug=models.DateTimeField(auto_now_add=False,verbose_name="year_ug")

	# ----------------------------------------Skill---------------------------------------
	skill =models.CharField(max_length=150,verbose_name="skill")
	area_of_skill=models.CharField(max_length=25,verbose_name="area_of_skill")

    # ---------------------------------------Experience-------------------------------


	exp = models.CharField(max_length=15,verbose_name="exp")





	created_date = models.DateTimeField(auto_now_add=True,verbose_name="Posted on")
	def __str__(self):
		return "{} - {}".format(self.author,self.phone,self.add,self.exp,self.email
			)
	class Meta:
		ordering = ['-created_date']


class Upload_resume(models.Model):
	author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "author ")
	resume=models.FileField(verbose_name="resume")
	Upload_date = models.DateTimeField(auto_now_add=True,verbose_name="Posted on")


	def __str__(self):
		return "{} - {}".format(self.author,self.resume,self.Upload_date)
	class Meta:
		ordering = ['-Upload_date']




		






		