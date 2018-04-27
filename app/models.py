from app import db
from app import ma

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(35), index=True, unique=True)
    name = db.Column(db.String(60), index=True)
    dept = db.Column(db.String(25), index=True)

    def __repr__(self):
        return '<User {}>'.format(self.email)

class ProfessorSchema(ma.Schema):
    class Meta:
        fields = ('name', 'email','dept')

professorSchema = ProfessorSchema()
professorSchema = ProfessorSchema(many=True)

'''
class OfficeHours(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, )
'''
