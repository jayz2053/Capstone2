from app import app
from app.modeles import Professor, professorSchema


@app.route('/')
@app.route('/index')
def index():
    return "What up bitches"

@app.route('/professor', methods=["GET"])
def getProfessor():
    all_prof = Professor.query.all()
    results = professorSchema.dump(all_prof)
    return jsonify(results.data)
