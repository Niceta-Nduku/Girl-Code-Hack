from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)





"""
#just python algorith for a rough idea
mentorlist = []
pofessionalList = []
#check if both mentor and student are available for mentorship
for professional in professionalList:
	if professional.mentor :
		if student.mentorship:

			#check other compatibility features only if both are available for mentorship

			if student.location.city == professional.location.city
				match += 1

			#check in the current student profile's interests match with any of the professionals
			for i in student.interests:
				for _ in professional.interests:
				match += 1
	#add mentor to the list if there are compatible
	if match >= 3 :
		mentorlist.append(professional)
#list of all mentors who matched
return mentorlist
"""




#tried to include sqlalchemy commands here
from sqlalchemy import and_
mentorlist = []

#if student is looking for a mentor
if student.mentorship :


	#every student interest is checked against all the professions by iteration
	for _ in student.interests:
		records = session.query(professional).filterby(and_(professional.interests == student.interests,professional.location==student.location,professional.mentor==true,))
		mentorlist.append(records)




