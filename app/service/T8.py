import datetime
from app.csv.index import calendar as calender_index
from app.common.commonUtil import df_update, df_read

def calendar_atom(arg_list):
    v_list_new = [str(x) for x in arg_list]
    year, month, day = arg_list[0], arg_list[1], arg_list[2]
    if (year < 2000 or year > 2100) and (month < 1 or month > 12) and (day < 1 or day > 31):
        return 'Illegal Case'
    if year < 2000 or year > 2100:
        return 'Year Exceed'
    if month < 1 or month > 12:
        return 'Month Exceed'
    if day < 1 or day > 31:
        return 'Day Exceed'
    try:
        _date = datetime.datetime.strptime('-'.join(v_list_new), '%Y-%m-%d').date()
    except Exception as e:
        return str(e)
    return str(_date + datetime.timedelta(days=1))

class T8:
    def __init__(self):
        pass

    @staticmethod
    def calendar(method_type):
        csv_path = calender_index[method_type]
        df, arg_start, arg_end = df_read(csv_path)
        output1 = []
        for i in range(0, len(df)):
            arg_list = df.iloc[i, arg_start:arg_end].values.tolist()
            output1.append(calendar_atom(arg_list))
        return df_update(df=df, csv_path=csv_path, actual_outputs=[output1], tester_name='Spidey Sandwich')


    @staticmethod
    def calendar_method_test(request):
        arg_list = [request['year'], request['month'], request['day']]
        return calendar_atom(arg_list)
