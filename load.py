import pandas as pd
from calculator.models import *

path = "/home/william/Documents/Python_Scripts/DnD_Project/virtual/"
file = path + 'chi_data.csv'

def readFile():
	df = pd.read_csv(file)
	return df

def addData():
	df = readFile()
	x = 0
	for index, row in df.iterrows():
		ls = []
		for i in range(1, len(row)):
			z = [float(row[i])]
			ls = ls + z
		try:
			ch = ChiTab(DegreeFreedom=int(row[0]), p_995=ls[0], p_99=ls[1], p_975=ls[2],\
				p_95=ls[3], p_9=ls[4], p_1=ls[5], p_05=ls[6], p_025=ls[7],\
				p_01=ls[8], p_005=ls[9])
			ch.save()
		except:
			x = x +1
	print(str(x) + ' Rows failed to be added to the database.')

def fullLoader():
	try:
		addData()
	except:
		print("Data Failed to Load")

			

