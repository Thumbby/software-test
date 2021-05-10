from flask_restplus import Namespace, Resource, fields
from app.model.T3 import model
from app.service.T3 import T3 as T3_service

api = Namespace('T3', description='佣金问题')
model = api.model('Comission', model=model)


@api.route('/commission/<method_type>')
@api.param('method_type', 'boundary-input | boundary-output')
@api.response(404, 'Method not found')
class Calendar(Resource):
    @api.doc('Commission Problem')
    def get(self, method_type):
        """
        佣金问题
        """
        return T3_service.commission(method_type)


@api.route('/commission/')
class CalenderBasic(Resource):
    @api.doc('Commission Problem Basic Method')
    @api.expect(model)
    def post(self):
        """
        佣金问题的基础实现
        """
        return T3_service.commission_method_test(api.payload)
