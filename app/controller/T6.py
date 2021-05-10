from flask_restplus import Namespace, Resource, fields
from app.model.T6 import model
from app.service.T6 import T6 as T6_service

api = Namespace('T6', description='电信收费问题')
model = api.model('Commission', model=model)


@api.route('/charge/<method_type>')
@api.param('method_type', 'boundary | equivalence | decision | final')
@api.response(404, 'Method not found')
class Calendar(Resource):
    @api.doc('Charge Problem')
    def get(self, method_type):
        """
        电信收费问题
        """
        return T6_service.charge(method_type)


@api.route('/charge/')
class CalenderBasic(Resource):
    @api.doc('Charge Problem Basic Method')
    @api.expect(model)
    def post(self):
        """
        电信收费问题的基础实现
        """
        return T6_service.charge_method_test(api.payload)



