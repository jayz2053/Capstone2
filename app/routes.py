from app import app
from json import dumps
from flask import jsonify, request, make_response
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
@app.route('/course', methods=["GET"])
def getClasses():
    all_class = Course.query.all()
    results = courseSchema.dump(all_class)

    return jsonify(results.data)

@app.route('/department/course/<string:dept>')
def getCoursesByDept(dept):
    courseList = Course.query.filter(Course.dept == dept.replace('-', ' ')).all()
    result = courseSchema.dump(courseList)

    return jsonify(result.data)

@app.route('/office', methods=['GET'])
def getOfficeHours():
    all_office = OfficeHours.query.all()
    results = officeSchema.dump(all_office)

    return jsonify(results.data)

@app.route('/professor', methods=["GET"])
def getProfessors():
    all_prof = Professor.query.all()
    results = professorSchema.dump(all_prof)

    return jsonify(results.data)

@app.route('/professor/<string:email_id>', methods=["GET"])
def getProfessor(email_id):
    uno_prof = Professor.query.filter(Professor.email == '{}@uwf.edu'.format(email_id)).all()
    result = professorSchema.dump(uno_prof)

    return jsonify(result.data)

@app.route('/professor/office/<string:email_id>', methods=["GET"])
def getProfessorOfficeHours(email_id):
    uno_prof = Professor.query.filter(Professor.email == '{}@uwf.edu'.format(email_id)).all()

    #print(uno_prof[0].dept)

    hoursOfProf = uno_prof[0].hours

    '''
    for item in hoursOfProf:
        print(item)
    '''
    results = officeSchema.dump(hoursOfProf)
    return jsonify(results.data)

@app.route('/professor/course/<string:email_id>', methods=["GET"])
def getCoursesByProfessor(email_id):
    uno_prof = Professor.query.filter(Professor.email == '{}@uwf.edu'.format(email_id)).all()

    profCourses = uno_prof[0].courses

    results = courseSchema.dump(profCourses)
    return jsonify(results.data)

@app.route('/department/professor/<string:dept>', methods=['GET'])
def getProfByDept(dept):

    profList = Professor.query.filter(Professor.dept == dept.replace('-', ' '))
    result = professorSchema.dump(profList)

    return jsonify(result.data)

@app.route('/department', methods=["GET"])
def getDepartment():
    ans = []

    for dept in db.session.query(Professor.dept).distinct():
        ans.append(dept[0])

    return jsonify({'results': ans})


@app.route('/destination', methods=["GET"])
def getDestination():
    all_dest = Destination.query.all()
    result = destinationSchema.dump(all_dest)

    return jsonify(result.data)

@app.route('/destination/<string:did>', methods=['GET'])
def getSingleDestination(did):
    uno_dest = Destination.query.filter(Destination.did == did)
    result = destinationSchema.dump(uno_dest)

    return jsonify(result.data)

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
    dept = request.json['dept']
    courseNum = request.json['courseNum']
    name = request.json['name']
    email = request.json['email']
    days = request.json['days']
    start_time = request.json['start_time']
    end_time = request.json['end_time']
    did = request.json['did']

    new_course = Course(crn, dept, courseNum, name, email, days, start_time, end_time, did)
    db.session.add(new_course)
    db.session.commit()

    return jsonify(new_course)
