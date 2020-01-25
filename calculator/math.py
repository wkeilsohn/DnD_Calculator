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

	def pFinder(freedeg, chi):
		c1 = ChiTab(DegreeFreedom=freedeg)
		c2 = ChiTab(DegreeFreedom=0)
		cdict = c1.to_dic()
		cdf = pd.from_dict(cdict)
		x = 0
		for index, row in cdf.iterrows():
			for i in row:
				if row[i] < chi:
					pass
				else:
					x = i
					break
		print(x)
		return 0.4
#		return pval