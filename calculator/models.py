from django.db import models

class ChiTab(models.Model):
	DegreeFreedom = models.IntegerField(null=False, blank=False)
	p_995 = models.DecimalField(null=False, blank=False, decimal_places=3, max_digits=7)
	p_99 = models.DecimalField(null=False, blank=False, decimal_places=3, max_digits=7)
	p_975 = models.DecimalField(null=False, blank=False, decimal_places=3, max_digits=7)
	p_95 = models.DecimalField(null=False, blank=False, decimal_places=3, max_digits=7)
	p_9 = models.DecimalField(null=False, blank=False, decimal_places=3, max_digits=7)
	p_1 = models.DecimalField(null=False, blank=False, decimal_places=3, max_digits=7)
	p_05 = models.DecimalField(null=False, blank=False, decimal_places=3, max_digits=7)
	p_025 = models.DecimalField(null=False, blank=False, decimal_places=3, max_digits=7)
	p_01 = models.DecimalField(null=False, blank=False, decimal_places=3, max_digits=7)
	p_005 = models.DecimalField(null=False, blank=False, decimal_places=3, max_digits=7)

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
