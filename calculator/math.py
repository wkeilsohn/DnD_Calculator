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
		ddist = len(refvals)
		if num == 0:
			val = refvals[num]
		elif num < ddist:
			val = refvals[num - 1]
		else:
			val = refvals[ddist - 1]
		return val

	def pFinder(freedeg, chi):
		freedeg = int(freedeg)
		c = ChiTab.objects.filter(DegreeFreedom=freedeg)
		for i in c:
			chils = i.to_ls()
		y = 0
		print(chi)
		for j in chils:
			if chi > j:
				y = y + 1
				pass
			else:
				break
		pval = chiSquare.mapper(y)
		return pval