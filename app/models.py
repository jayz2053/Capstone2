'''
LOOK INTO FURTHER REFACTORING OF MODELS AND ROUTES
USING SEPERATE FILES AND __INIT__.py

https://stackoverflow.com/questions/1944569/how-do-i-write-good-correct-package-init-py-files

'''


from app import db
from app import ma

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(35), unique=True)
    name = db.Column(db.String(60))
    dept = db.Column(db.String(25))
    hours = db.relationship('OfficeHours', backref='prof')
    courses = db.relationship('Course', backref = 'prof')

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
    did = db.Column(db.String(5), db.ForeignKey('destination.did'))                   # FOREIGN KEY
    email = db.Column(db.String(35), db.ForeignKey('professor.email'))                # FOREIGN KEY
    days= db.Column(db.String(5))
    start_time = db.Column(db.String(8))
    end_time = db.Column(db.String(8))


    def __init__(self, did, email, days, start, end):
        self.did = did
        self.email = email
        self.days = days
        self.start_time = start
        self.end_time = end

    def __repr__(self):
        return '<Hours {0}-{1} for {2}>'.format(self.start_time, self.end_time, self.email)

class OfficeSchema(ma.Schema):
    class Meta:
        fields = ('id', 'did', 'email', 'days', 'start_time', 'end_time')

officeSchema = OfficeSchema()
officeSchema = OfficeSchema(many=True)

class Destination(db.Model):
    did = db.Column(db.String(5), primary_key=True)
    destType = db.Column(db.String(15))
    description = db.Column(db.String(200))
    courses = db.relationship('Course', backref = 'destination')
    officeHours db.relationship('OfficeHous', backref = 'destination')


    def __repr__(self):
        return '<Destination {0} {1}>'.format(self.did, self.destType)

    def __init__(self, did, destType, description):
        self.did = did
        self.destType = destType
        self.description = description


class DestinationSchema(ma.Schema):
    class Meta:
        fields = ('did', 'destType', 'description')

destinationSchema = DestinationSchema()
destinationSchema = DestinationSchema(many=True)

class Course(db.Model):
    crn = db.Column(db.String(5), primary_key=True)
    dept = db.Column(db.String(20))
    courseNum = db.Column(db.String(7))
    name = db.Column(db.String(30))
    email = db.Column(db.String(35), db.ForeignKey('professor.email'))        #FOREIGN KEY
    days= db.Column(db.String(5))
    start_time = db.Column(db.String(8))
    end_time = db.Column(db.String(8))
    did = db.Column(db.String(5), db.ForeignKey('destination.did'))           #FOREIGN KEY

    def __repr__(self):
        return '<Course {0} {1}>'.format(self.crn, self.courseNum)

    def __init__(self, crn, dept, courseNum, name, email, days, start_time, end_time, did):
        self.crn = crn
        self.dept = dept
        self.courseNum = courseNum
        self.name = name
        self.email = email
        self.days = days
        self.start_time = start_time
        self.end_time = end_time
        self.did = did

class CourseSchema(ma.Schema):
    class Meta:
        fields = ('courseNum', 'dept', 'name', 'days', 'start_time', 'end_time', 'did')

courseSchema = CourseSchema()
courseSchema = CourseSchema(many=True)
