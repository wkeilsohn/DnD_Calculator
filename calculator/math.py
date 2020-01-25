import pandas as pd
from calculator.models import *

class chiSquare():

	def degFree(df):
		num = len(df.columns)
		freedeg = num - 1
		return freedeg

	def calcChi(df):
		dlen = len(df.columns)
		dvals = df.iloc[1].values.tolist()
		dsum = sum(dvals)
		dexpect = (dsum / dlen)
		chi = 0
		for i in dvals:
			z = (((i - dexpect)**2) / dexpect)
			chi = chi + z
		return chi

	def mapper(num):
		c = ChiTab.objects.filter(DegreeFreedom=0)
		for i in c:
			refvals = i.to_ls()
		val = refvals[num]
		return val

	def pFinder(freedeg, chi):
		c = ChiTab.objects.filter(DegreeFreedom=freedeg)
		for i in c:
			chils = i.to_ls()
		y = 0
		for j in chils:
			if chi > j:
				y = y + 1
				pass
			else:
				pval = chiSquare.mapper(y - 1)
		return pval