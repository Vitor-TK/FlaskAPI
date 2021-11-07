from flask import request
from flask_restplus import Resource
from src.config.restplus import api
from src.api.serializers.test_serializer import test_request, test_result
from src.services.test_service import create, change, delete, get
 

ns = api.namespace('api/test', description='Operations related to test')


@ns.route('')#refine rota
class TestCollection(Resource):
    @api.expect(test_request)#define parametro de entrada para a documentaçao do swagger
    @api.marshal_with(test_result)#define resultado da metodo 
    def post(self):
        """
        Create a new Test
        """ 
        test = create(request.json)
        return test 

 

@ns.route('/<int:id>')
class TestIDCollection(Resource): 
    @api.marshal_with(test_result)
    def get(self, id):
        """
        Get test by ID
        """ 
        test = get(id)
        return test 


    @api.expect(test_request)
    @api.marshal_with(test_result)
    def put(self, id):
        """
        Change student by ID
        """ 
        student = change(id,request.json)
        return student 
 
    @api.marshal_with(test_result)
    def delete(self, id):
        """
        Delete test by ID
        """ 
        test = delete(id)
        return test 