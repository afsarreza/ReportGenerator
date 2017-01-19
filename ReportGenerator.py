#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#ReportGenerator.py
#  
#  Copyright 2014 afsar <afsar@ubuntu>
#  
import Tkinter
import sys,string
import csv,os,sys
import Image
import PIL
import datetime	

from Tkconstants import * 
from Tkinter import Tk
from tkFileDialog import askopenfilename
import matplotlib.pylab as plt
from pylab import *
from pyPdf import PdfFileWriter, PdfFileReader
from reportlab.pdfgen import canvas
from StringIO import StringIO
from pyPdf import *
from reportlab.pdfgen import *
from ttk import Frame, Button, Label, Style


import MySQLdb

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Frame, Spacer,PageBreak
from reportlab.lib import colors,styles
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A3, A4, landscape, portrait,letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.platypus.flowables import Image


filename =""

class Simple_app(Tkinter.Tk):
	
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		#matplotlib.pylab.__init__(self)
		filename=""
		self.parent=parent
		self.initialize()
	
	def initialize(self):
		self.grid()
		print self.grid_size()
		self.geometry("1025x600+100+100")
		
		self.update_idletasks()
		
		self.grid_columnconfigure(0,pad=5)
		self.grid_columnconfigure(1,pad=5)
		self.grid_columnconfigure(2,pad=5)
		self.grid_columnconfigure(3,pad=5)
		self.grid_columnconfigure(4,pad=5)
		
		self.grid_rowconfigure(0,pad=5)
		self.grid_rowconfigure(1,pad=5)
		self.grid_rowconfigure(2,pad=5)
		self.grid_rowconfigure(3,pad=5)
		self.grid_rowconfigure(4,pad=5)
		self.grid_rowconfigure(5,pad=5)
		self.grid_rowconfigure(6,pad=5)
		self.grid_rowconfigure(7,pad=5)
		self.grid_rowconfigure(8,pad=5)
		self.grid_rowconfigure(9,pad=5)
		self.grid_rowconfigure(10,pad=5)
		
		
		self.OpenFilebutton=Tkinter.Button(self,text="Open File",command=self.OpenFile)
		self.OpenFilebutton.grid(row=0,column=0,padx=5,pady=5)
		
		self.Graphbutton=Tkinter.Button(self,text="Generate Graph",command=self.GenerateGraph)
		self.Graphbutton.grid(row=1,column=0,padx=5,pady=5)
		
		
		
		self.projectNameLabel=Tkinter.Label(self,text="Project Name")
		self.projectNameLabel.grid(row=2,column=0)
		self.projectNameEntry=Tkinter.Entry(self)
		self.projectNameEntry.grid(row=2,column=1)
		
		
		self.unitNameLabel=Tkinter.Label(self,text="Unit Name")
		self.unitNameLabel.grid(row=3,column=0)
		self.unitNameEntry=Tkinter.Entry(self)
		self.unitNameEntry.grid(row=3,column=1)
		
		self.testNameLabel=Tkinter.Label(self,text="Test Name")
		self.testNameLabel.grid(row=4,column=0)
		self.testNameEntry=Tkinter.Entry(self)
		self.testNameEntry.grid(row=4,column=1)
		
		self.testTypeLabel=Tkinter.Label(self,text="Test Type")
		self.testTypeLabel.grid(row=5,column=0)
		self.testTypeEntry=Tkinter.Entry(self)
		self.testTypeEntry.grid(row=5,column=1)
		
		self.specificationLabel=Tkinter.Label(self,text="Speification")
		self.specificationLabel.grid(row=6,column=0)
		self.specificationEntry=Tkinter.Entry(self)
		self.specificationEntry.grid(row=6,column=1)
		
		self.testDurationLabel=Tkinter.Label(self,text="Test Duration")
		self.testDurationLabel.grid(row=7,column=0)
		self.testDurationEntry=Tkinter.Entry(self)
		self.testDurationEntry.grid(row=7,column=1)
		
		self.altitudeLabel=Tkinter.Label(self,text="Altitude")
		self.altitudeLabel.grid(row=8,column=0)
		self.altitudeEntry=Tkinter.Entry(self)
		self.altitudeEntry.grid(row=8,column=1)
		
		self.fileLabel=Tkinter.Label(self,text="File Name")
		self.fileLabel.grid(row=2,column=3)
		self.fileEntry=Tkinter.Entry(self)
		self.fileEntry.grid(row=2,column=4)
		
		#self.axisLabel=Tkinter.Label(self,text="Axis")
		#self.axisLabel.grid(row=9,column=2)
		#self.axisEntry=Tkinter.Entry(self)
		#self.axisEntry.grid(row=9,column=3)
		
		self.Createbutton=Tkinter.Button(self,text="Create Project",command=self.insertProjectValues)
		self.Createbutton.grid(row=10,column=0,padx=5,pady=5)
		
		self.labelVariable=Tkinter.StringVar()
		
		self.Submitbutton=Tkinter.Button(self,text="Submit File Data",command=self.insertfilename)
		self.Submitbutton.grid(row=3,column=4,padx=5,pady=5)
		
		self.Submitbutton=Tkinter.Button(self,text="Generate Report",command=self.generateReport)
		self.Submitbutton.grid(row=10,column=4,padx=5,pady=5)
		
		label=Tkinter.Label(self,textvariable=self.labelVariable,anchor="s",fg="white",bg="blue")
		label.grid(row=0,column=3)
		
		self.okButton=Tkinter.Button(self,text="Ok",fg="green")
		self.okButton.grid(row=15,column=0)
		
		self.cancelButton=Tkinter.Button(self,text="Exit",fg="red",command=lambda:self.destroy())
		self.cancelButton.grid(row=15,column=4)
		
		self.resizable(False,True)
	
	def OpenFile(self):
		global filename
		filename=askopenfilename()
		return filename
	
	def TestWindow(self):
		pass
	
	def ThermalEntryWindow(self):
		pass
	
		
	def Cancel(self):
		pass		
	
	def GMIEntryWindow(self):
		pass
		#self.entry.bind("<Return>",self.OnPressEnter)
		
		
	def VibrationEntryWindow(self):
		pass
		
	def getConnection(self):
		try:
			self.db=MySQLdb.connect("127.0.0.1","root","1786","missile")
			
			print "Connected to the server"
			self.cursor=self.db.cursor()
			return self.cursor
		except:
			print "couldn't  connect"
		
		
	def insertProjectValues(self):
		self.projectName=self.projectNameEntry.get()
		print self.projectName
		self.unitName=self.unitNameEntry.get()
		print self.unitName
		self.testName=self.testNameEntry.get()
		print self.testName
		self.testType=self.testTypeEntry.get()
		print self.testType
		self.specification=self.specificationEntry.get()
		print self.specification
		self.testduration=self.testDurationEntry.get()
		print self.testduration
		self.altitude=self.altitudeEntry.get()
		print self.altitude
		self.projectdate=str(datetime.datetime.now().date())
		print self.projectdate
		
		self.cursor=self.getConnection()	
		
		try:
			#self.cursor.execute('''CREATE DATABASE missile IF NOT EXISTS''')
			#self.cursor.execute('''USE missile''')
			
			self.cursor.execute('''create table IF NOT EXISTS project(project_id INT AUTO_INCREMENT,
																		project_name VARCHAR(45),
																		unit_name VARCHAR(45),
																		test_name VARCHAR(45),
																		test_type VARCHAR(45),
																		specification VARCHAR(45),
																		test_duration VARCHAR(45),
																		altitude VARCHAR(45),
																		curdate VARCHAR(45),
																		PRIMARY KEY(project_id))''')
									
			self.cursor.execute('''create table IF NOT EXISTS filetype(file_id INT AUTO_INCREMENT,
																		p_id INT,
																		filename VARCHAR(45),
																		CONSTRAINT FOREIGN KEY (p_id) REFERENCES project(project_id),
																		PRIMARY KEY(file_id))''')
			
			#self.cursor.execute('''create table IF NOT EXISTS axis(axis_id INT NOT NULL AUTO_INCREMENT,
			#															f_id INT NOT NULL,
			#															axisname VARCHAR(10) NOT NULL,
			#															CONSTRAINT FOREIGN KEY (f_id) REFERENCES filetype(file_id),
			#															PRIMARY KEY(axis_id))''')																					
			
			
			self.cursor.execute('''create table IF NOT EXISTS navigation(nav_id INT AUTO_INCREMENT,
																		f_id INT NOT NULL,
																		 velX DOUBLE,
																		 velY DOUBLE,
																		 velZ DOUBLE,
																		 posX DOUBLE,
																		 posY DOUBLE,
																		 posZ DOUBLE,
																		 tempX DOUBLE,
																		 tempY DOUBLE,
																		 tempZ DOUBLE,
																		 time DOUBLE,
																		 status DOUBLE,
																		CONSTRAINT FOREIGN KEY (f_id) REFERENCES filetype(file_id),
																		PRIMARY KEY(nav_id))''')
			print "table created"
			self.cursor.execute("""INSERT INTO project (project_id,project_name,unit_name,test_name,test_type,specification,test_duration,altitude,curdate) VALUES (default,'%s','%s','%s','%s','%s','%s','%s','%s')""" %(self.projectName,self.unitName,self.testName,self.testType,self.specification,self.testduration,self.altitude,self.projectdate))
			#print "Inserted the value"
			#self.insertfilename()
			self.db.commit()
			#self.insertfilename()
		except:
			print "coudn't insert"
			self.db.rollback()
		finally:
			self.db.close()	
	
	def fetchrow(self):
		self.proj_id=self.cursor.fetchall()
		for self.row in self.proj_id:
			self._pid=self.row[0]
		return self._pid	
			
	def insertfilename(self):
		self.filename=self.fileEntry.get()
		print self.filename
		self.cursor=self.getConnection()
		#self.cursor.execute("""DECLARE @NewProjectID INT""")
		#self.cursor.execute("""SELECT @NewProjectID = SCOPE_IDENTITY() from project """)
		self.cursor.execute("""SELECT MAX(project_id) from project""")
		#self.proj_id=self.cursor.fetchall()
		#for self.row in self.proj_id:
		#	self.pid=self.row[0]
		self.pid=self.fetchrow()
		#print self.pid 
		self.cursor.execute("""INSERT INTO filetype(file_id,p_id,filename) VALUES (default,'%s','%s')""" %(self.pid,self.filename))
		print "Inserted the value"
		self.insertNavigationData()
		#self.db.commit()
		#self.insertAxis()
		
	#def insertAxis(self):
	#	self.axis=self.axisEntry.get()
	#	self.cursor.execute("""SELECT MAX(file_id) from filetype""")
	#	self.fid=self.fetchrow()
	#	print self.fid	
	#	self.cursor.execute("""INSERT INTO axis(axis_id,f_id,axisname) VALUES (default,'%s','%s')""" %(self.fid,self.axis))
	#	print "Inserted the value"
	#	self.db.commit()
	#	self.insertNavigationData()	
	
	def insertNavigationData(self):
		self.file_name=self.OpenFile()
		print self.file_name
		self.cursor.execute("""SELECT MAX(file_id) from filetype""")
		self.max_file_id=self.fetchrow()
		print self.max_file_id
		#self.cursor.execute("""LOAD DATA INFILE self.file_name
		#						INTO TABLE intern.navigation
		#						 COLUMNS TERMINATED BY '\t' 
		#						 OPTIONALLY ENCLOSED BY '""'
		#						 ESCAPED BY '""'
		#						 LINES TERMINATED BY '\n'
		#						 IGNORE 1 ROWS""")
		#self.max_file_id=1
		with open(self.file_name,"r") as f:
			self.reader=csv.reader(f,delimiter="\t")
			for self.row in self.reader:
				if len(self.row):
					print self.row[0],self.row[1],self.row[2],self.row[3],self.row[4],self.row[5],self.row[6],self.row[7],self.row[8],self.row[9],self.row[10]
					
					self.cursor.execute("""INSERT INTO navigation(nav_id ,f_id , velX ,velY,velZ,posX,posY,posZ,tempX,tempY,tempZ,time,status) VALUES (default,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" %(self.max_file_id,self.row[0],self.row[1],self.row[2],self.row[3],self.row[4],self.row[5],self.row[6],self.row[7],self.row[8],self.row[9],self.row[10]))
					self.db.commit()
	
	
	def generateReport(self):
		
		self.pdfReportPages = "Report.pdf"
		
		self.doc = SimpleDocTemplate(self.pdfReportPages, pagesize=A4,rightMargin=65,leftMargin=65,bottomMargin=85,topMargin=10)

	# container for the "Flowable" objects
		self.elements = []
		self.styles=getSampleStyleSheet()
		self.styleN = self.styles["Normal"]
		self.styleH = self.styles["Heading2"]
		self.logo1=Image("/home/afsar/Desktop/prog_py/rci.jpg",width=75,height=75)
		self.logo2=Image("/home/afsar/Desktop/prog_py/DRDO.png",width=75,height=75)
		self.logo1.hAlign="CENTER"
		self.logo2.hAlign="CENTER"
		
		
		self.elements.append(Paragraph("Report On Projects",self.styleH))

	# Make heading for each column and start data list
		self.column1Heading = "Vx"
		self.column2Heading = "Vy"
		self.column3Heading = "Vz"
		self.column4Heading = "Px"
		self.column5Heading = "Py"
		self.column6Heading = "Pz"
		self.column7Heading = "tempX"
		self.column8Heading = "tempy"
		self.column9Heading = "tempZ"
		self.column10Heading = "time"
		self.column11Heading = "status"
		
		self.projectColumn1Header= "project Name"
		self.projectColumn2Header= "Unit Name"
		self.projectColumn3Header= "Test Name"
		self.projectColumn4Header="Test Type"
		self.projectColumn5Header= "Specification"
		self.projectColumn6Header ="Test Duration"
		self.projectColumn7Header ="Altitude"
		self.projectColumn8Header ="Date"

		self.signature1="Director"
		self.signature2="Head Officer"
	# Assemble data for each column using simple loop to append it into data list
		
				
		self.cursor=self.getConnection()
		
		self.cursor.execute('''SELECT * FROM project''')
		self.projectTableResults=self.cursor.fetchall()
		
		#self.cursor.execute('''SELECT MAX(project_id) FROM project''')
		#self.max_num=self.fetchrow()
		
		self.cursor.execute('''SELECT * FROM filetype''')
		self.fileTableResults=self.cursor.fetchall()
		
		for self.projectTableResult in self.projectTableResults:
			self.elements.append(self.logo2)
			self.elements.append(self.logo1)
			self.data1=[[self.projectColumn1Header,self.projectColumn2Header,self.projectColumn3Header,self.projectColumn4Header,self.projectColumn5Header,self.projectColumn6Header,self.projectColumn7Header,self.projectColumn8Header]]

			self.data1.append([self.projectTableResult[1],self.projectTableResult[2],self.projectTableResult[3],self.projectTableResult[4],self.projectTableResult[5],self.projectTableResult[6],self.projectTableResult[7],self.projectTableResult[8]])
				
			self.projectTable = Table(self.data1,repeatRows=1,repeatCols=0)
			self.projectTable.hAlign = 'CENTRE'
		
			self.tbStyle = TableStyle([
								('GRID',(0,0),(-1,-1),0.5,colors.black),
								('TEXTCOLOR',(0,0),(-1,-1),colors.black),
								('VALIGN',(0,0),(-1,-1),'TOP'),
								('LINEBELOW',(0,0),(-1,-1),1,colors.black),
								('BOX',(0,0),(-1,-1),2,colors.pink),
								('BOX',(0,0),(-1,-1),2,colors.black)])
			self.tbStyle.add('BACKGROUND',(0,0),(7,0),colors.lightblue)
			#self.tbStyle.add('BACKGROUND',(0,1),(-1,-1),colors.white)
		
			self.projectTable.setStyle(self.tbStyle)
			self.elements.append(self.projectTable)
			del self.data1[:]
			
			self.elements.append(Spacer(1,36))
			self.cursor.execute("""SELECT filetype.filename FROM filetype join project on filetype.p_id=project.project_id where project.project_id=%s""",(self.projectTableResult[0],))
			self.fileTableResults=self.cursor.fetchall()
			for self.fileTableResult in self.fileTableResults:
			
				self.cursor.execute("""select velX,velY,velZ,posX,posY,posZ,tempX,tempY,tempZ,time,status from navigation join filetype on filetype.file_id=navigation.f_id join project on filetype.p_id =project.project_id where project.project_id = %s AND filetype.filename=%s""",(self.projectTableResult[0],self.fileTableResult[0],))
				self.navTableResults=self.cursor.fetchall()
				#select nav_id,f_id from navigation join filetype on filetype.file_id=navigation.f_id join project on filetype.p_id=project.project_id where project.project_id=2;
				
				self.elements.append(Paragraph(self.fileTableResult[0],self.styleH))
				self.data = [[self.column1Heading,self.column2Heading,self.column3Heading,self.column4Heading,self.column5Heading,self.column6Heading,self.column7Heading,self.column8Heading,self.column9Heading,self.column10Heading,self.column11Heading]]
			
				for self.navTableResult in self.navTableResults:
					self.data.append([self.navTableResult[0],self.navTableResult[1],self.navTableResult[2],self.navTableResult[3],self.navTableResult[4],self.navTableResult[5],self.navTableResult[6],self.navTableResult[7],self.navTableResult[8],self.navTableResult[9],self.navTableResult[10]])
			
				
			
				self.tableThatSplitsOverPages = Table(self.data,repeatRows=1,repeatCols=0)
				self.tableThatSplitsOverPages.hAlign = 'CENTRE'
		
				self.tblStyle = TableStyle([ 
							('GRID',(0,0),(-1,-1),0.5,colors.black),
							('TEXTCOLOR',(0,0),(-1,-1),colors.black),
						   ('VALIGN',(0,0),(1,1),'TOP'),
						   ('LINEBELOW',(0,0),(-1,-1),1,colors.black),
						   ('BOX',(0,0),(-1,-1),2,colors.pink),
						   ('BOX',(0,0),(-1,-1),2,colors.black)])
				self.tblStyle.add('BACKGROUND',(0,0),(10,0),colors.lightblue)
				self.tblStyle.add('BACKGROUND',(0,1),(-1,-1),colors.white)
		
				self.tableThatSplitsOverPages.setStyle(self.tblStyle)
				self.elements.append(self.tableThatSplitsOverPages)
				self.elements.append(Spacer(1,36))
			#self.sig=[]
			self.elements.append(Paragraph("Signature",self.styleH))
			self.elements.append(PageBreak())
			del self.data[:]
			

		self.doc.build(self.elements)				
		
	def GenerateGraph(self):
		global filename
		list1=[]
		list2=[]
		try:
			with open(filename,"r") as f:
				reader=csv.reader(f,delimiter=":")
				for row in reader:
					if len(row):
						list1.append(row[0])
						list2.append(row[1])
					else:
						break
			f.close()
		except:
			print "Provide the file name"
		
			
		fig = plt.figure()
		axes=fig.add_axes([0.1,0.1,0.4,0.4])    
		axes.plot(list1,list2,'r')
		axes.set_xlabel("Acceleration")
		axes.set_ylabel("Time")
		fig.savefig("graph.pdf",bbox_inches='tight')
		print "graph.pdf reached"
		self.labelVariable.set("Graph has been drawn")
		InsertLogo()
		print " InsertLogo function called"

def InsertLogo():
	imgTemp = StringIO()
	imgDoc = canvas.Canvas(imgTemp)

		# Draw image on Canvas and save PDF in buffer
	imgPath = "/home/afsar/Desktop/prog_py/rci.jpg"
	imgDoc.drawImage(imgPath, 200, 350, 100, 100)    ## at (399,760) with size 160x160
	imgDoc.save()

		# Use PyPDF to merge the image-PDF into the template
	page = PdfFileReader(file("/home/afsar/Desktop/prog_py/graph.pdf","rb")).getPage(0)
	overlay = PdfFileReader(StringIO(imgTemp.getvalue())).getPage(0)
	page.mergePage(overlay)

		#Save the result
	output = PdfFileWriter()
	output.addPage(page)
	output.write(file("/home/afsar/Desktop/prog_py/output.pdf","w"))	
	print "You pressed the button"
	os.system('xdg-open "output.pdf"')		




		
def main():
	
	app=Simple_app(None)
	app.title("Data Visualization Tool")
	app.mainloop()
	
	

if __name__ == '__main__':
	main()	
