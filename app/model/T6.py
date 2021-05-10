from flask_restplus import fields

model = {
    'talk_time_month': fields.Integer(required=True, description='当月通话时间'),
    'unpaid_num_year': fields.Integer(required=True, description='年度累计未按时缴费的次数'),
}

MODELS = []
