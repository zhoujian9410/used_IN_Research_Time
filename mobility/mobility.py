#!/usr/bin/python

import xlrd
import numpy as np
import matplotlib.pyplot as plt

def data_ach(number):
	data=xlrd.open_workbook("data_transfer.xlsx")
	table=data.sheet_by_index(0)
	vg=np.zeros((number,1))
	ids=np.zeros((number,1))
	vg=table.col_values(0)
	ids=table.col_values(2)
	return vg,ids

def get_gm(number,vg,ids):
	gm=np.zeros((number,1))
	for i in range(number):
		if i==0:
			gm[i]=(ids[i+1]-ids[i])/(vg[i+1]-vg[i])
		elif i==number-1:
			gm[i]=(ids[i]-ids[i-1])/(vg[i]-vg[i-1])
		else :
			gm[i]=(ids[i+1]-ids[i-1])/(vg[i+1]-vg[i-1])
	return gm

def get_mobility(gm,ex,th):
	l,w=raw_input("please enter the channel length and width:\n").split()
	l=float(l)
	w=float(w)
	vds=raw_input("please enter the bias:\n")
	vds=float(vds)
	cox=ex*8.854*100/th
	n=len(gm)
	ufe=np.zeros((n,1))
	ufe=gm*l/(w*vds*cox)
	ufe=ufe*(10**9)
	return ufe

def paixu(ufe):
	umax=np.zeros((10,1))
	ll=len(ufe)
	ub=ufe
	for i in range(10):
		umax[i]=ub[0]
		for j in range(ll):
			if ub[j]>=umax[i]:
				umax[i]=ub[j]
				num=j
		ub[num]=0
	for i in range(10):
		print umax[i]
	return umax

def average(umax):
	a,b=raw_input("the next procedure will calculate the aveage of the mobility,you could enter two number,which the first number indicate the removed high points,the 2nd one indicate the removed low points:\n").split()
	a=long(a)
	b=long(b)
	umax1=umax
	number=len(umax1)-1
	for i in range(a):
		umax1[i]=0
	for i in range(b):
		umax1[number-i]=0
#	for i in range(number+1):
#		print umax1[i]
	ave=0
	for i in range(number+1):
		ave=ave+umax1[i]
	ave=ave/(number+1-a-b)
	print '\n\n\n\t\t'
	print '\t\t',ave,"cm^2 V^-1 s^-1"	

 
	

def main():
	data=xlrd.open_workbook("data_transfer.xlsx")
	table=data.sheet_by_index(0)
	vg=table.col_values(0)

	number=len(vg)
	vg=np.zeros((number,1))
	ids=np.zeros((number,1))
	gm=np.zeros((number,1))

	vg=table.col_values(0)
	ids=table.col_values(2)

	gm=get_gm(number,vg,ids)
	ex=3.9
	si_type=raw_input("please enter the Oxide type(a:for SiO2i(3.9)&b:for Al2O3(10)&c:for BN(4)):\n")
	if si_type=='a':
		ex=3.9
	elif si_type=='b':
		ex=10
	elif si_type=='c':
		ex=4
	else :
		print "error input with Oxide type"
	thickness=raw_input("please enter the oxide thickness:\n")
	thickness=long(thickness)
	ufe=get_mobility(gm,ex,thickness)
	umax=np.zeros((10,1))
	umax=paixu(ufe)
	average(umax)
#	print ufe

main()
