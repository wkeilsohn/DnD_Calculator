from django.db import models

class ChiTab(models.Model):
	DegreeFreedom = models.IntegerField()
	p_995 = models.IntegerField()
	p_99 = models.IntegerField()
	p_975 = models.IntegerField()
	p_975 = models.IntegerField()
	p_95 = models.IntegerField()
	p_9 = models.IntegerField()
	p_1 = models.IntegerField()
	p_05 = models.IntegerField()
	p_025 = models.IntegerField()
	p_01 = models.IntegerField()
	p_005 = models.IntegerField()