from app import db
from app import ma

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(35), unique=True)
    name = db.Column(db.String(60))
    dept = db.Column(db.String(25))
    hours = db.relationship('OfficeHours', backref = 'office_hours')
    teaches = db.relationship('Course', backref = 'teaches')

    def __init__(self, email, name, dept):
        self.email = email
        self.name = name
        self.dept = dept

    def __repr__(self):
        return '<User {}>'.format(self.email)

class ProfessorSchema(ma.Schema):
    class Meta:
        fields = ('name', 'email','dept')

professorSchema = ProfessorSchema()
professorSchema = ProfessorSchema(many=True)


class OfficeHours(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    did = db.Column(db.String(5), db.ForeignKey('destination.did'))
    email = db.Column(db.String(35), db.ForeignKey('professor.email'))
    days= db.Column(db.String(5))
    start_time = db.Column(db.String(8))
    end_time = db.Column(db.String(8))
    #professor = db.relationship("Professor", back_populates="officeHours")

    def __repr__(self):
        return '<Hours {0}-{1} for {3}>'.format(self.start_time, self.end_time, self.email)

class OfficeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'did', 'email', 'days', 'start_time', 'end_time')

officeSchema = OfficeSchema()
officeSchema = OfficeSchema(many=True)

class Destination(db.Model):
    did = db.Column(db.String(5), primary_key=True)
    destType = db.Column(db.String(15))
    description = db.Column(db.String(200))
    hours = db.relationship('OfficeHours', backref='office')
    classes = db.relationship('Course', backref='courses')

    def __repr__(self):
        return '<Destination {0} {1}>'.format(self.did, self.destType)

class DestinationSchema(ma.Schema):
    class Meta:
        fields = ('did', 'destType', 'description')

destinationSchema = DestinationSchema()
destinationSchema = DestinationSchema(many=True)

class Course(db.Model):
    crn = db.Column(db.String(5), primary_key=True)
    courseNum = db.Column(db.String(7))
    name = db.Column(db.String(30))
    email = db.Column(db.String(35), db.ForeignKey('professor.email'))
    days= db.Column(db.String(5))
    start_time = db.Column(db.String(8))
    end_time = db.Column(db.String(8))
    did = db.Column(db.String(5), db.ForeignKey('destination.did'))
