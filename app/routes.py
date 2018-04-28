from app import app
from flask import jsonify, request
from app.models import Professor, professorSchema
from app.models import OfficeHours, officeSchema
from app import db
#from app.models import


@app.route('/')
@app.route('/index')
def index():
    return "What up bitches"

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

@app.route('/professor', methods=['POST'])
def addProfessor():
    email = request.json['email']
    name = request.json['name']
    dept = request.json['dept']

    new_professor = Professor(email, name, dept)
    db.session.add(new_professor)
    db.session.commit()
    return jsonify(new_professor)
