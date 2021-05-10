import os

BASE_DIR = os.path.dirname(__file__)

csv_dir = {
    'calendar': ['boundary', 'equivalence-weak-general', 'equivalence-strong-general', 'equivalence-weak-robust',
                 'equivalent-strong-robust'],
    'triangle': ['boundary', 'equivalence'],
    'commission': ['boundary'],
    'charge': ['boundary', 'equivalence', 'decision'],
    'sales': ['statement', 'judge', 'condition', 'judge-condition', 'condition-combination'],
    'printer': ['printer', 'printer-robust']
}

calendar = {
    'boundary': BASE_DIR + '/T8/calendar-boundary.csv',
    'equivalence': BASE_DIR + '/T8/calendar-equivalence.csv',
}

triangle = {
    'boundary': BASE_DIR + '/T1/triangle-boundary.csv',
    'equivalence': BASE_DIR + '/T1/triangle-equivalence.csv'
}

commission = {
    'boundary': BASE_DIR + '/T3/commission-boundary.csv',
}

charge = {
    'boundary': BASE_DIR + '/T6/charge-boundary.csv',
    'equivalence': BASE_DIR + '/T6/charge-equivalence.csv',
    'decision': BASE_DIR + '/T6/charge-decision.csv',
    'final': BASE_DIR + '/T6/charge.csv'
}

sales = {
    'statement': BASE_DIR + '/q8/sales-statement-cov.csv',
    'judge': BASE_DIR + '/q8/sales-judge-cov.csv',
    'condition': BASE_DIR + '/q8/sales-condition-cov.csv',
    'judge-condition': BASE_DIR + '/q8/sales-judge-condition-cov.csv',
    'condition-combination': BASE_DIR + '/q8/sales-condition-combination-cov.csv'
}

printer = {
    'printer': BASE_DIR + '/q6/printer-transition-tree.csv',
    'printer-robust': BASE_DIR + '/q6/printer-transition-tree-robust.csv'
}

csv_dir2 = {
    'calendar': calendar,
    'triangle': triangle,
    'commission': commission,
    'charge': charge,
    'sales': sales,
    'printer': printer
}
