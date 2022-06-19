
def dict_mat(data):
    return {'E': data[0], 'G': data[1], 'μ': data[2], 'ρ': data[3]}


materials = {
    'Si<001>': dict_mat([130e9, 50e9, 0.28, 2320]),
    'Si<011>': dict_mat([150e9, 70e9, 0.06, 2320]),
    'Si<010>': dict_mat([130e9, 50e9, 0.28, 2320]),

    'polySi': dict_mat([169e9, 69e9, 0.22, 2100]),

    'SiC<001>': dict_mat([270e9, 103e9, 0.31, 3200]),
    'SiC<011>': dict_mat([350e9, 162e9, 0.08, 3200]),
    'SiC<010>': dict_mat([270e9, 103e9, 0.31, 3200]),
}

task1_1 = {
    '1': [materials.get('Si<001>'),  100e-6, 5e-6, 0.9e-6, 1],
    '2': [materials.get('SiC<010>'), 200e-6, 8e-6, 1.0e-6, 2],
    '3': [materials.get('polySi'),   300e-6, 6e-6, 0.8e-6, 3],
    '4': [materials.get('Si<011>'),  400e-6, 3e-6, 0.5e-6, 4],
    '5': [materials.get('SiC<011>'), 500e-6, 9e-6, 1.2e-6, 5],
    '6': [materials.get('Si<010>'),  600e-6, 4e-6, 0.7e-6, 6],
}

task1_2 = {
    '1': [materials.get('Si<001>'),  100e-6, 5e-6, 0.9e-6, 1, 0.1],
    '2': [materials.get('SiC<010>'), 200e-6, 8e-6, 1.0e-6, 2, 0.2],
    '3': [materials.get('polySi'),   300e-6, 6e-6, 0.8e-6, 3, 0.3],
    '4': [materials.get('Si<011>'),  400e-6, 3e-6, 0.5e-6, 4, 0.4],
    '5': [materials.get('SiC<011>'), 500e-6, 9e-6, 1.2e-6, 5, 0.5],
    '6': [materials.get('Si<010>'),  600e-6, 4e-6, 0.7e-6, 6, 0.6],
}

task1_3 = {
    '1': [materials.get('Si<001>'),  100e-6, 5e-6, 0.9e-6, 1e-6,  0.02e-6, -0.01e-6],
    '2': [materials.get('SiC<010>'), 200e-6, 8e-6, 1.0e-6, 2e-6,  0.06e-6, -0.02e-6],
    '3': [materials.get('polySi'),   300e-6, 6e-6, 0.8e-6, 3e-6,  0.08e-6, -0.03e-6],
    '4': [materials.get('Si<011>'),  400e-6, 3e-6, 0.5e-6, 4e-6,  0.03e-6, -0.04e-6],
    '5': [materials.get('SiC<011>'), 500e-6, 9e-6, 1.2e-6, 5e-6,  0.07e-6, -0.05e-6],
    '6': [materials.get('Si<010>'),  600e-6, 4e-6, 0.7e-6, 15e-6, 0.12e-6, -0.06e-6],
}

task2 = {
    '1': [materials.get('Si<001>'),  100e-6, 5e-6, 0.9e-6, 0.1e-6],
    '2': [materials.get('SiC<010>'), 200e-6, 8e-6, 1.0e-6, 0.2e-6],
    '3': [materials.get('polySi'),   300e-6, 6e-6, 0.8e-6, 0.3e-6],
    '4': [materials.get('Si<011>'),  400e-6, 3e-6, 0.5e-6, 0.4e-6],
    '5': [materials.get('SiC<011>'), 500e-6, 9e-6, 1.2e-6, 0.5e-6],
    '6': [materials.get('Si<010>'),  600e-6, 4e-6, 0.7e-6, 0.6e-6],
}

task3 = {
    '1': [materials.get('Si<001>'),  5.1e-6, 1e-10, 20, 70],
    '2': [materials.get('SiC<010>'), 4.0e-6, 2e-10, 30, 80],
    '3': [materials.get('polySi'),   2.0e-6, 3e-10, 40, 90],
    '4': [materials.get('Si<011>'),  5.1e-6, 4e-10, 50, 100],
    '5': [materials.get('SiC<011>'), 4.0e-6, 5e-10, 60, 110],
    '6': [materials.get('Si<010>'),  5.1e-6, 6e-10, 70, 120],
}

task4 = {
    '1': ['pr', 'zos', materials.get('Si<001>'),  100e-6, 5e-6, 0.9e-6, 0.1e-6],
    '2': ['kr', 'zos', materials.get('SiC<010>'), 200e-6, 8e-6, 8.0e-6, 0.2e-6],
    '3': ['pr', 'roz', materials.get('polySi'),   300e-6, 6e-6, 0.8e-6, 0.3e-6],
    '4': ['kr', 'roz', materials.get('Si<011>'),  400e-6, 3e-6, 3.0e-6, 0.4e-6],
    '5': ['pr', 'zos', materials.get('SiC<011>'), 500e-6, 9e-6, 1.2e-6, 0.5e-6],
    '6': ['kr', 'roz', materials.get('Si<010>'),  600e-6, 4e-6, 4.0e-6, 0.6e-6],
}

task5 = {
    '1': ['kon', materials.get('Si<001>'),  100e-6, 5e-6, 0.9e-6],
    '2': ['mis', materials.get('SiC<010>'), 200e-6, 8e-6, 1.0e-6],
    '3': ['kon', materials.get('polySi'),   300e-6, 6e-6, 0.8e-6],
    '4': ['mis', materials.get('Si<011>'),  400e-6, 3e-6, 0.5e-6],
    '5': ['kon', materials.get('SiC<011>'), 500e-6, 9e-6, 1.2e-6],
    '6': ['mis', materials.get('Si<010>'),  600e-6, 4e-6, 0.7e-6],
}
