from src.models import db
from src.models.course import Course
from src.models.student import Student
from src.config.restplus import  json_abort
from sqlalchemy.exc import SQLAlchemyError 

### AUTOR SERVICE
### gerenciar as regras de negocio e CRUD do author
###

def create(data):
    try:

        course_name = data.get('course_name')
        if not course_name:
            json_abort(400,"Course Name is required")

        study_area = data.get('study_area')
        if not study_area:
            json_abort(400,"Study Area is required")

 
        course = Course(course_name=course_name,study_area=study_area)
        db.session.add(course)
        db.session.commit()

        return course

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def get(id):
    try:
        course = Course.query.filter_by(id=id).first()
        course.list_students = Student.query.filter_by(course_id=id).all()
        if not course:
            json_abort(400,"Course not found")
        else:
            return course

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def change(id, data):
    try:
        
        course = Course.query.filter_by(id=id).first()

        if not course:
            json_abort(400,"Course not found")
        else:

            course_name = data.get('course_name')
            if not course_name:
                json_abort(400,"Course Name is required")

            study_area = data.get('study_area')
            if not study_area:
                json_abort(400,"Study Area is required")


            course.course_name = course_name
            course.study_area = study_area
            
            db.session.delete(course)
            db.session.commit()
        
            return course

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def delete(id):
    try:
        
        course = Course.query.filter_by(id=id).first()

        if not course:
            json_abort(400,"Course not found")
        else:
            db.session.delete(course)
            db.session.commit()
        
            return course

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)