from src.models.test import Tests
from src.models import db
from src.models.student import Student
from src.config.restplus import  json_abort
from sqlalchemy.exc import SQLAlchemyError
import datetime

#importa a consulta de author e incluir um apelido ao get para evitar conflito com o get do post
from src.services.course_service import get as get_course

### AUTOR SERVICE
### gerenciar as regras de negocio e CRUD do Post
###

def create(data):
    try:

        name = data.get('name')
        if not name:
            json_abort(400,"name is required")

        age = data.get('age')
        if not age:
            json_abort(400,"age is required")

        cpf = data.get('cpf')
        if not cpf:
            json_abort(400,"cpf is required")

        course_id = data.get('course_id')
        if not course_id:
            json_abort(400,"course_id is required")

        course = get_course(course_id)
 
        created = datetime.datetime.now()

        student = Student(name=name,created=created, course_id=course_id,course=course,age=age,cpf=cpf)
        db.session.add(student)
        db.session.commit()

        return student

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def get(id):
    try:
        student = Student.query.filter_by(id=id).first()
        student.list_tests = Tests.query.filter_by(student_id=id).all()
        if not student:
            json_abort(400,"Student not found")
        else:
            return student

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def change(id, data):
    try:
        
        student = Student.query.filter_by(id=id).first()

        if not student:
            json_abort(400,"Student not found")
        else:

            name = data.get('name')
            if not name:
                json_abort(400,"name is required")
 
            student.name = name 
            
            db.session.delete(student)
            db.session.commit()
        
            return student

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def delete(id):
    try:
        
        student = Student.query.filter_by(id=id).first()

        if not student:
            json_abort(400,"Student not found")
        else:
            db.session.delete(student)
            db.session.commit()
        
            return student

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)