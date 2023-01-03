import random
def start(args, hkubeapi):
    print('algorithm: range start')
    input = args['input'][0]
    array = [random.random() for _ in range(input)]
    return array

# temp_args_dict = {
#     'input': [8]
# }

# print(start(temp_args_dict, None))
