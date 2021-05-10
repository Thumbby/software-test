from app.csv.index import charge as charge_index
from app.common.commonUtil import df_update, df_read


def charge_atom(arg_list):
    monthly_fee, cost_per_min = 25, 0.15
    talk_time_month, unpaid_num_year, unpaid_cost_across_year = \
        arg_list[0], arg_list[1], arg_list[2]
    cost = monthly_fee
    if talk_time_month < 0 or talk_time_month > 44640 or unpaid_num_year < 0 or unpaid_num_year > 11 :
        return 'error'
    if talk_time_month <= 60 and unpaid_num_year <= 1:
        cost += talk_time_month * cost_per_min * (1 - 0.01)
    elif 60 < talk_time_month <= 120 and unpaid_num_year <= 2:
        cost += talk_time_month * cost_per_min * (1 - 0.015)
    elif 120 < talk_time_month <= 180 and unpaid_num_year <= 3:
        cost += talk_time_month * cost_per_min * (1 - 0.02)
    elif 180 < talk_time_month <= 300 and unpaid_num_year <= 3:
        cost += talk_time_month * cost_per_min * (1 - 0.025)
    elif talk_time_month > 300 and unpaid_num_year <= 6:
        cost += talk_time_month * cost_per_min * (1 - 0.03)
    else:
        cost += talk_time_month * cost_per_min
    return float('%.5f' % cost)




class T6:
    def __init__(self):
        pass

    @staticmethod
    def charge(method_type):
        csv_path = charge_index[method_type]
        df, arg_start, arg_end = df_read(csv_path)
        output1 = []
        for i in range(0, len(df)):
            arg_list = df.iloc[i, arg_start:arg_end].values.tolist()
            output1.append(charge_atom(arg_list))
        return df_update(df=df, csv_path=csv_path, actual_outputs=[output1], tester_name='Spidey Sandwich')

    @staticmethod
    def charge_method_test(request):
        arg_list = [request['talk_time_month'], request['unpaid_num_year']]
        return charge_atom(arg_list)
