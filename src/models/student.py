from . import db
from .course import Course  

#configura modelo de dados do POST
class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    cpf = db.Column(db.String(255))
    created = db.Column(db.DateTime) 
    course_id = db.Column(
        db.Integer, db.ForeignKey('course.id', ondelete='CASCADE'))
    course = db.relationship('Course')

    def __str__(self):
        return self.description

    def get_post_id(self):
        return self.id