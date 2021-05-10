import os

BASE_DIR = os.path.dirname(__file__)

csv_dir = {
    'calendar': ['boundary', 'equivalence-weak-general', 'equivalence-strong-general', 'equivalence-weak-robust',
                 'equivalent-strong-robust'],
    'triangle': ['boundary', 'equivalence'],
    'commission': ['boundary'],
    'charge': ['boundary', 'equivalence', 'decision'],
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
