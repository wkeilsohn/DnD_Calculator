from django.db import models

class ChiTab(models.Model):
	DegreeFreedom = models.IntegerField()
	p_995 = models.FloatField()
	p_99 = models.FloatField()
	p_975 = models.FloatField()
	p_95 = models.FloatField()
	p_9 = models.FloatField()
	p_1 = models.FloatField()
	p_05 = models.FloatField()
	p_025 = models.FloatField()
	p_01 = models.FloatField()
	p_005 = models.FloatField()

	def to_dic(self):
		return {'DegreeFreedom':self.DegreeFreedom, 'p_995':self.p_995,	'p_99':self.p_99, 'p_975':self.p_975,\
		'p_95':self.p_95, 'p_9':self.p_9, 'p_1':self.p_1, 'p_05':self.p_05, 'p_025':self.p_025,\
		'p_01':self.p_01, 'p_005':self.p_005}


'''
class SampleData(models.Model):
	Side = models.IntegerField()
	Number_of_Observations = models.IntegerField()

	def to_dic(self):
		return{'Side':self.Side, 'Number_of_Observations':self.Number_of_Observations}
'''
