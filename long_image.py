import random as np


def my_actual_algorithm(some_input):
    return [np.random_integer(2,6)**4466.4343 for _ in range(input)]


def start(args, hkubeapi):
    print('algorithm: range start')
    input = args['input'][0]
    result = my_actual_algorithm(input)
    return result

