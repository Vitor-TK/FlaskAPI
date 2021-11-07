from flask import request
from flask_restplus import Resource
from src.config.restplus import api
from src.api.serializers.course_serializer import course_request, course_result
from src.services.course_service import create, change, delete, get
 

ns = api.namespace('api/course', description='Operations related to course')

 
@ns.route('')#define rota
class CourseCollection(Resource):
    @api.expect(course_request)#define parametro de entrada para a documentaçao do swagger
    @api.marshal_with(course_result)#define resultado da metodo 
    def post(self):
        """
        Create a new Course
        """ 
        course = create(request.json)
        return course 

 

@ns.route('/<int:id>')
class CourseIDCollection(Resource): 
    @api.marshal_with(course_result)
    def get(self, id):
        """
        Get course by ID
        """ 
        course = get(id)
        return course 


    @api.expect(course_request)
    @api.marshal_with(course_result)
    def put(self, id):
        """
        Change course by ID
        """ 
        course = change(id,request.json)
        return course 
 
    @api.marshal_with(course_result)
    def delete(self, id):
        """
        Delete course by ID
        """ 
        course = delete(id)
        return course 