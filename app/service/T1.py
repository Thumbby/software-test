import datetime
from app.csv.index import triangle as triangle_index
from app.common.commonUtil import df_update, df_read


def triangle_atom(arg_list):
    a, b, c = arg_list[0], arg_list[1], arg_list[2]
    if a > 20 or b > 20 or c > 20:
        return '数值越界'
    if a <= 0 or b <= 0 or c <= 0:
        return '数值越界'
    if a + b > c and a + c > b and b + c > a:
        if a == b or a == c or b == c:
            if a == b and b == c:
                return '等边三角形'
            elif a * a + b * b == c * c or b * b + c * c == a * a or a * a + c * c == b * b:
                return '等腰直角三角形'
            else:
                return '等腰三角形'
        if a * a + b * b == c * c or b * b + c * c == a * a or a * a + c * c == b * b:
            return '直角三角形'
        else:
            return '普通三角形'
    else:
        return '非三角形'


class T1:
    def __init__(self):
        pass

    @staticmethod
    def triangle(method_type):
        csv_path = triangle_index[method_type]
        df, arg_start, arg_end = df_read(csv_path=csv_path)
        output1 = []
        for i in range(0, len(df)):
            arg_list = df.iloc[i, arg_start:arg_end].values.tolist()
            output1.append(triangle_atom(arg_list))
        return df_update(df=df, csv_path=csv_path, actual_outputs=[output1], tester_name='Spidey Sandwich')

  
    @staticmethod
    def triangle_method_test(request):
        arg_list = [request['edge1'], request['edge2'], request['edge3']]
        return triangle_atom(arg_list)
