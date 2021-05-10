from flask_restplus import fields

triangle_model = {
    'edge1': fields.Float(required=True, description='边1'),
    'edge2': fields.Float(required=True, description='边2'),
    'edge3': fields.Float(required=True, description='边3')
}

MODELS = []
