from . import db 

#configura modelo de dados do Course
class Course(db.Model):
    __tablename__ = 'course'

    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(255))
    study_area = db.Column(db.String(255)) 


    def __str__(self):
        return self.course_name

    def get_user_id(self):
        return self.id

  

