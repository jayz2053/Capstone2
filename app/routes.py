from app import app
from flask import jsonify, request
from app.models import Professor, professorSchema
from app.models import OfficeHours, officeSchema
#from app.models import


@app.route('/')
@app.route('/index')
def index():
    return "What up bitches"

@app.route('/professor', methods=["GET"])
def getProfessor():
    all_prof = Professor.query.all()
    results = professorSchema.dump(all_prof)
    return jsonify(results.data)

@app.route('/professor/<email_id>', methods=["GET"])
def getProfessor(email_id):
    uno_prof = Professor.query.(Professor.email == '{}@uwf.edu'.format(email_id))
    result = professorSchema.dump(uno_prof)
    return jsonfiy(results.data)
