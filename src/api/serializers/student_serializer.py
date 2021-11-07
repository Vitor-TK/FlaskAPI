from flask_restplus import fields
from src.config.restplus import api
from src.api.serializers.test_serializer import test_result

student_request = api.model('Student Request', {
    'name': fields.String(required=True, description='student name'),
    'age': fields.Integer(required=True, description='student age'),
    'cpf': fields.String(required=True, description='student cpf'),
    'course_id': fields.Integer(required=True, description='student course ID ')
})

student_result = api.model('Student Result', {
    'id': fields.Integer(required=True, description='Student Id'),
    'created': fields.String(required=True, description='date student created'),
    'name': fields.String(required=True, description='student name'),
    'age': fields.Integer(required=True, description='student age'),
    'cpf': fields.String(required=True, description='student cpf'),
    'course_id': fields.Integer(required=True, description='student course ID'),
    'list_tests': fields.List(fields.Nested(test_result), description="student tests")
    
})
