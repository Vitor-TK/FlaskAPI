from src.models import db
from src.models.test import Tests
from src.config.restplus import  json_abort
from sqlalchemy.exc import SQLAlchemyError
import datetime

#importa a consulta de author e incluir um apelido ao get para evitar conflito com o get do post
from src.services.student_service import get as get_student
### AUTOR SERVICE
### gerenciar as regras de negocio e CRUD do Post
###

def create(data):
    try:

        title = data.get('title')
        if not title:
            json_abort(400,"title is required")

        test_grade = data.get('test_grade')
        if not test_grade:
            json_abort(400,"test grade is required")

        concept = data.get('concept')
        if not concept:
            json_abort(400,"concept is required")

        student_id = data.get('student_id')
        if not student_id:
            json_abort(400,"student_id is required")

        student = get_student(student_id)
 
        created = datetime.datetime.now()

        test = Tests(title=title,created=created, student_id=student_id,student=student,test_grade=test_grade,concept=concept)
        db.session.add(test)
        db.session.commit()

        return test

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def get(id):
    try:
        test = Tests.query.filter_by(id=id).first()

        if not test:
            json_abort(400,"Test not found")
        else:
            return test

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)

def change(id, data):
    try:
        
        test = Tests.query.filter_by(id=id).first()

        if not test:
            json_abort(400,"Test not found")
        else:

            title = data.get('title')
            if not title:
                json_abort(400,"title is required")
 
            test.title = title 
            
            db.session.delete(test)
            db.session.commit()
        
            return test

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)


def delete(id):
    try:
        
        test = Tests.query.filter_by(id=id).first()

        if not test:
            json_abort(400,"Test not found")
        else:
            db.session.delete(test)
            db.session.commit()
        
            return test

    except SQLAlchemyError as err: 
        db.session.rollback()
        error = str(err.__dict__['orig'])
        json_abort(500, error)