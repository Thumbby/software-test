from flask_restplus import Api

from app.controller.demo import api as demo_api
from app.controller.T1 import api as T1_api
from app.controller.T3 import api as T3_api
from app.controller.T6 import api as T6_api
from app.controller.T8 import api as T8_api
from app.controller.show import api as show_csv_api
api = Api(
    title='Software Testing Visual Platform',
    version='v1.0',
    description='Software Testing Visual Platform Api'
)

api.add_namespace(demo_api, path='/demo')
api.add_namespace(T1_api, path='/T1')
api.add_namespace(T3_api, path='/T3')
api.add_namespace(T6_api, path='/T6')
api.add_namespace(T8_api, path='/T8')
api.add_namespace(show_csv_api, path='/show-csv')
