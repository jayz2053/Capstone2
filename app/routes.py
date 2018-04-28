from app import app
from flask import jsonify, request
from app.models import Professor, professorSchema
from app.models import OfficeHours, officeSchema
from app.models import Destination, destinationSchema
from app.models import Course, courseSchema
from app import db
#from app.models import


@app.route('/')
@app.route('/index')
def index():
    return "Hello World!"

#-----  GET ROUTES
@app.route('/professor', methods=["GET"])
def getProfessors():
    all_prof = Professor.query.all()
    results = professorSchema.dump(all_prof)
    return jsonify(results.data)

@app.route('/professor/<string:email_id>', methods=["GET"])
def getProfessor(email_id):
    uno_prof = Professor.query.filter(Professor.email == '{}@uwf.edu'.format(email_id))
    result = professorSchema.dump(uno_prof)
    return jsonify(result.data)

@app.route('/department', methods=["GET"])
def getDepartment():

    deptlist = []

    for dept in db.session.query(Professor.dept).distinct():
        deptlist.append(dept)

    return({ans: deptlist})

#-----  POST ROUTES
@app.route('/professor', methods=['POST'])
def addProfessor():
    email = request.json['email']
    name = request.json['name']
    dept = request.json['dept']

    new_professor = Professor(email, name, dept)
    db.session.add(new_professor)
    db.session.commit()
    return jsonify(new_professor)

@app.route('/office', methods=['POST'])
def addOfficeHours():
    did = request.json['did']
    email = request.json['email']
    days =  request.json['days']
    start = request.json['start']
    end = request.json['end']

    new_office_hours = OfficeHours(did, email, days, start, end)
    db.session.add(new_office_hours)
    db.session.commit()
    return jsonify(new_office_hours)

@app.route('/destination', methods=['POST'])
def addDestination():
    did = request.json['did']
    destType = request.json['destType']
    description = request.json['description']

    new_destination = Destination(did, destType, description)
    db.session.add(new_destination)
    db.session.commit()

    return jsonify(new_destination)

@app.route('/course', methods=['POST'])
def addCourse():
    crn = request.json['crn']
    courseNum = request.json['courseNum']
    name = request.json['name']
    email = request.json['email']
    days = request.json['days']
    start_time = request.json['start_time']
    end_time = request.json['end_time']
    did = request.json['did']

    new_course = Course(crn, courseNum, name, email, days, start_time, end_time, did)
    db.session.add(new_course)
    db.session.commit()

    return jsonify(new_course)
