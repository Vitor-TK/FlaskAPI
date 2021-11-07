from flask_restplus import fields
from src.config.restplus import api


test_request = api.model('Test Request', {
    'title': fields.String(required=True, description='test title'),
    'test_grade': fields.Float(required=True, description='test grade'),
    'concept': fields.String(required=True, description='test concept'),
    'student_id': fields.Integer(required=True, description='test student ID ')
})

test_result = api.model('Test Result', {
    'id': fields.Integer(required=True, description='test Id'),
    'title': fields.String(required=True, description='test title'),
    'test_grade': fields.Float(required=True, description='test test_grade'),
    'concept': fields.String(required=True, description='test concept'),
    'student_id': fields.Integer(required=True, description='test student ID'),
    'created': fields.String(required=True, description='date test created')
})
