from flask_restplus import Namespace, Resource, fields
from app.model.T1 import triangle_model as T1_model
from app.service.T1 import T1 as T1_service

api = Namespace('T1', description='判断三角形类型')
T1_model = api.model('Triangle', model=T1_model)


@api.route('/triangle/<method_type>')
@api.param('method_type', 'boundary | equivalence')
@api.response(404, 'Method not found')
class Triangle(Resource):
    @api.doc('Triangle Problem')
    def get(self, method_type):
        """
        三角形问题
        """
        return T1_service.triangle(method_type)


@api.route('/triangle/')
class TriangleBasic(Resource):
    @api.doc('Triangle Problem Basic Method')
    @api.expect(T1_model)
    def post(self):
        """
        三角形问题的基础实现
        """
        return T1_service.triangle_method_test(api.payload)


