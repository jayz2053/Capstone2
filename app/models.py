from app import db
from app import ma

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(35), unique=True)
    name = db.Column(db.String(60))
    dept = db.Column(db.String(25))
    hours = db.relationship('OfficeHours', back_populates='professor')

    def __repr__(self):
        return '<User {}>'.format(self.email)

class ProfessorSchema(ma.Schema):
    class Meta:
        fields = ('name', 'email','dept')

professorSchema = ProfessorSchema()
professorSchema = ProfessorSchema(many=True)


class OfficeHours(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    did = db.Column(db.String(5), unique=True, index=True)
    email = db.Column(db.String(35),db.ForeignKey('professor.email'))
    days= db.Column(db.String(5))
    start_time = db.Column(db.String(8))
    end_time = db.Column(db.String(8))
    professor = db.relationship("Professor", back_populates="officeHours")

    def __repr__(self):
        return '<Hours {0}-{1} for {3}>'.format(self.start_time, self.end_time, self.email)

class OfficeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'did', 'email', 'days', 'start_time', 'end_time')

officeSchema = OfficeSchema()
officeSchema = OfficeSchema(many=True)
