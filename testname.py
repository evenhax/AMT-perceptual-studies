
#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os


# def get_file_name(file_dir):
# 	name_list = []
# 	for root, dirs, files in os.walk(file_dir):
# 		for file in files:
# 			if os.path.splitext(file)[1] == '.jpg':
# 				name_list.append(os.path.join(root, file))
# 	# print(name_list)
# 	name_list.sort()
# 	print(name_list)
# 	return name_list
#
#
# # list3 stores all true nums
# def arrange2lists(aname_list):
# 	list1 = aname_list[0:self.__total]
# 	list2 = aname_list[self.__total:self.__total + self.__total]
# 	list3 = [self.__true_val] * self.__total
# 	for i in range(self.__total):
# 		if i % 3 == 0 or i % 7 == 0:
# 			m = list1[i]
# 			list1[i] = list2[i]
# 			list2[i] = m
# 			list3[i] = 1 - self.__true_val
# 	print(list1)
# 	print(list2)
# 	print(list3)
# 	return list1, list2, list3


def delblankline(infile, outfile):
	infopen = open(infile, 'r',encoding="utf-8")
	outfopen = open(outfile, 'w',encoding="utf-8")
	db = infopen.read()
	outfopen.write(db.replace(' ','\n'))
	infopen.close()
	outfopen.close()

def txt2list(filename,mylist1,mylist2):
	i=0
	with open(filename, "r") as f:
		for line in f.readlines():
			# print(type(line))
			line = line.strip('\n') #delete the '\n'
			print(type(line))
			if i%2==0:
				mylist1.append(str(line))
			else:
				mylist2.append(str(line))
			i=i+1
	print(mylist1)
	print(mylist2)
	return mylist1,mylist2

def listshuffle(l1,l2,true_val):
	size=len(l1)
	l3=[true_val]*size
	for i in range(size):
		if i % 3 == 0 or i % 7 == 0:
			m = l1[i]
			l1[i] = l2[i]
			l2[i] = m
			l3[i] = 1 - true_val
	return l1,l2,l3


l1=[]
l2=[]
delblankline("namelist.txt","change.txt")
txt2list("change.txt",l1,l2)
