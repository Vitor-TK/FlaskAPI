from . import db
from .student import Student 

#configura modelo de dados do POST
class Tests(db.Model):
    __tablename__ = 'SchoolTests'

    id = db.Column(db.Integer, primary_key=True) 
    title = db.Column(db.String(255))
    test_grade = db.Column(db.Float)
    concept = db.Column(db.String(255))
    created = db.Column(db.DateTime) 
    student_id = db.Column(
        db.Integer, db.ForeignKey('student.id', ondelete='CASCADE'))
    student = db.relationship('Student')

    def __str__(self):
        return self.description

    def get_post_id(self):
        return self.id