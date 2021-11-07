from flask_restplus import fields
from src.config.restplus import api
from src.api.serializers.student_serializer import student_result


course_request = api.model('Author Request', {
    'course_name': fields.String(required=True, description='text post') ,
    'study_area': fields.String(required=True, description='text post') 
})

course_result = api.model('Author Result', {
    'id': fields.Integer(required=True, description='Post Id'),
    'course_name': fields.String(required=True, description='text post') ,
    'study_area': fields.String(required=True, description='text post'),
    'list_students': fields.List(fields.Nested(student_result), description="course students") 
})
