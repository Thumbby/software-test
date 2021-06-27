from flask_restplus import Namespace, Resource, fields
from app.model.T8 import calender_model as T8_model
from app.service.T8 import T8 as T8_service

api = Namespace('T8', description='万年历问题')
T8_model = api.model('Calender', model=T8_model)



@api.route('/calendar/<method_type>')
@api.param('method_type',
           'boundary | equivalence-weak-general ｜ equivalence-strong-general ｜ equivalence-weak-robust ｜ equivalence-strong-robust')
@api.response(404, 'Method not found')
class Calendar(Resource):
    @api.doc('Calendar Problem')
    def get(self, method_type):
        """
        万年历问题
        """
        return T8_service.calendar(method_type)



@api.route('/calendar/', strict_slashes=False)
class CalenderBasic(Resource):
    @api.doc('Calender Problem Basic Method')
    @api.expect(T8_model)
    def post(self):
        """
        万年历问题的基础实现
        """
        return T8_service.calendar_method_test(api.payload)
