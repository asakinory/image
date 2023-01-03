def start(args, hkubeapi):
    print('algorithm: range start')
    input = args['input'][0]
    array = [i*2.2 for i in input]
    return array