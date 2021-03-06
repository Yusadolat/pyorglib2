import os
import shutil
class organize: #class
	def organizer(self,newpath,folder_name,choice):	#organizes the files
		if not os.path.exists(folder_name):
			print "Folder Does Not Exist"
			return
		if os.listdir(folder_name)==[]:
			print "Folder is Empty"
			return
		files=os.listdir(folder_name)	#select all files from the folder
		for file_name in files:
			if(file_name.find(".")==-1):
				extension=" "
			else:
				extension=file_name.split(".")[-1]	#find extension
			source=folder_name+'/'+file_name	#folder where all the files are present
			destination=newpath+'/'+extension	#folder where all the files are to be copied or moved
			if not os.path.exists(destination): #check if destination folder already exist
				os.makedirs(destination)
			if not os.path.exists(destination+'/'+file_name):	#check if file already present in destination
				if(choice=="copy"):	#copy operation
					shutil.copy(source,destination)
				if(choice=="move"): #move operation
					shutil.move(source,destination)
			else:
					print "Cannot "+choice+": "+file_name+" already exists"
