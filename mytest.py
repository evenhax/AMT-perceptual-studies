#!/usr/bin/python
# -*- coding: UTF-8 -*-
import PIL.Image
from PIL import ImageTk
import tkinter as tk
from tkinter import *
import testname

#TOTAL=TEST_NUM+TRAIN_NUM

class Test:

	# your path
	__train_num=2
	__test_num=4
	__test_time=1000
	__total=__train_num+__test_num
	__name_path='testname'
	__txt_path="namelist.txt"
	__txt_change="namechange.txt"
	__mask_path='mask.jpg'
	__a_list=[]
	__b_list=[]
	__c_list=[]
	__true_val=0
	__bttn=0
	__user_rec = {}  # save the result
	for i in range(__train_num+__test_num):
		__user_rec["pair_"+str(i)]=3
		print(__user_rec)


	#fetch the file names
	# def __get_file_name(self,file_dir):
	# 	name_list=[]
	# 	for root, dirs, files in os.walk(file_dir):
	# 		for file in files:
	# 			if os.path.splitext(file)[1] == '.jpg':
	# 				name_list.append(os.path.join(root, file))
	# 	# print(name_list)
	# 	name_list.sort()
	# 	print(name_list)
	# 	return name_list
	#
	# # list3 stores all true nums
	# def __arrange2lists(self,aname_list):
	# 	list1=aname_list[0:self.__total]
	# 	list2=aname_list[self.__total:self.__total+self.__total]
	# 	list3=[self.__true_val]*self.__total
	# 	for i in range(self.__total):
	# 		if i%3==0 or i%7==0 :
	# 			m=list1[i]
	# 			list1[i]=list2[i]
	# 			list2[i]=m
	# 			list3[i]=1-self.__true_val
	# 	print(list1)
	# 	print(list2)
	# 	print(list3)
	# 	return list1,list2,list3

	def __get_corresponse(self):
		a=[]
		b=[]
		testname.delblankline(self.__txt_path,self.__txt_change)
		a,b=testname.txt2list(self.__txt_change,self.__a_list,self.__b_list)
		self.__a_list,self.__b_list,self.__c_list=testname.listshuffle(a,b,self.__true_val)

	def initial_test(self):
		self.__get_corresponse()
		path_a = self.__a_list[0]
		path_b = self.__b_list[0]

		self.__bttn=0
		'''
		The Total window is divided into 2 parts, 
		for imgs and buttons respectively
		'''
		window = tk.Tk()
		window.title("choose your prefer")

		# the 1st part of my frame
		frm_img = tk.Frame(window)
		frm_img.pack(side='top')
		frm_l = tk.Frame(frm_img)
		frm_r = tk.Frame(frm_img)
		frm_l.pack(side='left')
		frm_r.pack(side='right')
		tk.Label(frm_l, text='img A').pack()
		tk.Label(frm_r, text='img B').pack()
		s01 = PIL.Image.open(self.__name_path+'/'+path_a)
		img01 = ImageTk.PhotoImage(s01)
		label_imgl = Label(frm_l, image=img01, width=150, height=150)
		label_imgl.pack(side='left')
		s02 = PIL.Image.open(self.__name_path+'/'+path_b)
		img02 = ImageTk.PhotoImage(s02)
		label_imgr = Label(frm_r, image=img02, width=150, height=150)
		label_imgr.pack(side='right')

		# the 2nd part of my frame
		frm_butt = tk.Frame(window)
		frm_butt.pack(side='bottom')
		radiovar = tk.StringVar()
		textvar = StringVar()
		def save_selec():
			self.__user_rec["pair_" + str(self.__bttn)] = int(radiovar.get())
			print(type(self.__bttn))
			print(self.__bttn)
			# print(type(self.__c_list[self.__bttn]))
			# print(type(radiovar.get()))
			if self.__bttn<self.__train_num:
				if self.__c_list[self.__bttn] == int(radiovar.get()):
					textvar.set('Training: Yes, you are right !')
				else:
					textvar.set('Training: Sorry, you are wrong !')
			elif self.__bttn>=self.__train_num and self.__bttn< self.__test_num:
				textvar.set('Please choose the real one in 1 second')
		label_warning=Label(frm_butt,textvariable=textvar)
		textvar.set('Please choose the real one in 1 second')
		label_warning.pack()
		r1 = tk.Radiobutton(frm_butt, text='I like A', variable=radiovar, value=0, command=save_selec)
		r1.pack()
		r2 = tk.Radiobutton(frm_butt, text='I like B', variable=radiovar, value=1, command=save_selec)
		r2.pack()

		def gomask():
			s01 = PIL.Image.open(self.__mask_path)
			img01 = ImageTk.PhotoImage(s01)
			label_imgl.configure(image=img01)
			label_imgl.image = img01

			s02 = PIL.Image.open(self.__mask_path)
			img02 = ImageTk.PhotoImage(s02)
			label_imgr.configure(image=img02)
			label_imgr.image = img02

		# button counter
		def button_count():
			# r1.Checked = false
			# r2.Checked=false
			if self.__bttn==self.__train_num:
				textvar.set('Please choose the real one in 1 second')
			if self.__user_rec["pair_" + str(self.__bttn)]==3:
				textvar.set('YOU MUST click on the little circle!!')
			else:
				if self.__bttn<self.__train_num:
					textvar.set(' ')
				if (self.__bttn == (self.__total - 1)):
					print(self.__user_rec)
				self.__bttn += 1
				if (self.__bttn < self.__total):
					path_a = self.__a_list[self.__bttn]
					path_b = self.__b_list[self.__bttn]

					s01 = PIL.Image.open(self.__name_path+'/'+path_a)
					img01 = ImageTk.PhotoImage(s01)
					label_imgl.configure(image=img01)
					label_imgl.image = img01
					label_imgl.after(self.__test_time, gomask)

					s02 = PIL.Image.open(self.__name_path+'/'+path_b)
					img02 = ImageTk.PhotoImage(s02)
					label_imgr.configure(image=img02)
					label_imgr.image = img02
					label_imgr.after(self.__test_time, gomask)

		# window.update_idletasks()

		mybutt = tk.Button(frm_butt, text='Next', command=button_count)
		mybutt.pack()

		window.mainloop()


if __name__ == '__main__':
	Test().initial_test()



