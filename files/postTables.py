import csv
import requests

ip = "http://188.166.97.39"

'''DONE'''
# Definitions for posting to each table
def postCourse(course):
	with open('{}.csv'.format(course), 'rb') as f:
		reader = csv.reader(f)
		
		#main loop for data processsing
		for row in reader:
			
			#build json payload
			payload = {"crn": row[0], "dept": row[3], "courseNum": row[1], "name": row[2], "email": row[4], "days": row[5], "start_time": row[6], "end_time": row[7], "did": row[8] }
			
			#post to address
			r = requests.post('{0}/{1}'.format(ip, course), json = payload)
				

'''DONE'''
def postProfessor(professor):
	with open('{}.csv'.format(professor), 'rb') as f:
		reader = csv.reader(f)
		
		for row in reader:
			payload = {"email" : row[0], "name" : row[1], "dept" : row[2] }
			r = requests.post('{0}/{1}'.format(ip, professor), json = payload)
			
			
'''DONE'''
def postDest(dest):
	with open('{}.csv'.format(dest), 'rb') as f:
		reader = csv.reader(f)
		
		for row in reader:
			payload = {"did" : row[0], "destType" : row[1] , "description" : row[2] }
			r = requests.post('{0}/{1}'.format(ip, dest), json = payload)

'''DONE'''
def postOffice(office):	
	with open('{}.csv'.format(office), 'rb') as f:
		reader = csv.reader(f)
		
		for row in reader:
			payload = {"email": row[0], "did" : row[1], "days": row[2], "start": row[3], "end": row[4] }
			r = requests.post('{0}/{1}'.format(ip, office), json = payload)

# Definition for main simply defining route names and calling functions
def main():
	course = 'course'
	professor = 'professor'
	dest = 'destination'
	office = 'office'
	
	#postCourse(course)
	#postProfessor(professor)
	#postDest(dest)
	postOffice(office)
	
	
main()
