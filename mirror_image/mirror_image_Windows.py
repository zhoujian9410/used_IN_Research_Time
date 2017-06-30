#! C:\Python27
import numpy as np
import cv2
import os
import sys
from time import sleep
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def mirror(img):
	size=img.shape
	img_lr=np.zeros((size[0],size[1],size[2]),dtype=np.uint8)
	for i in range(size[0]):
		for j in range(size[1]):
			img_lr[i,j]=img[i,size[1]-1-j]

	return img_lr

def get_pic():
	current_path=os.getcwd()
	current_path=current_path+'\\'
	pathdir=os.listdir(current_path)
	num_cal=0
	for alldir in pathdir:
		child=os.path.join('%s%s'%(current_path,alldir))
		#child=child.decode('gbk')
		i=1
		while((child[-1*i]!='.')and(i<len(child))):
			i=i+1
		num=i
		ch_index=[]

		for i in range(num):
			ch_index.append(child[i-num])

		number = len(child)-num
		name=[]
		for i in range(number):
			name.append(child[i])
		name="".join(name)
		ch_index="".join(ch_index)
		name=name+"_mirrored"+ch_index
		cpath_len=len(current_path)
		ch_len=len(child)
		na_len=len(name)
		len1=ch_len-cpath_len
		len2=na_len-cpath_len
		a=[]
		for i in range(len1):
			a.append(child[cpath_len+i])
		b=[]
		for i in range(len2):
			b.append(name[cpath_len+i])
		a="".join(a)
		b="".join(b)


#judge the type of the child 
		if (ch_index=='.jpg')or(ch_index=='.bmp')or(ch_index=='.jpeg')or(ch_index=='.png'):
			num_cal=num_cal+1
			img=cv2.imread(child)
			print "%d"%num_cal
			print " . the "+a+" have been changed to "+ b+"!\n "
			size1=img.shape
			img1=np.zeros((size1),dtype=np.uint8)
			img1=mirror(img)

			#	print name
			cv2.imwrite(name, img1)

#def eachfile(filepath):
#        pathdir=os.listdir(filepath)
#        for alldir in pathdir:
#               child=os.path.join('%s%s'%(filepath,alldir))
#                print child.decode('gbk')
#	a=os.getcwd()


def main():
        print "the picture in this folder will be mirrored right now"
	get_pic()
        sleep(3)
        sys.exit()

main()
