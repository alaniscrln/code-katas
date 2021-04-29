import re

def range_parser(string):

    parts = re.split(', |,', string)
    tokenA = re.compile('^\d*-\d*$')
    tokenB = re.compile('^\d*-\d*:\d*$')
    result = []
    
    for val in parts:

        if tokenA.match(val) is not None:
            token = [int(x) for x in val.split('-')]
            result += [i for i in range(token[0], token[1] + 1)]

        elif tokenB.match(val) is not None:
            token = [int(x) for x in re.split('-|:', val)]
            result += ([i for i in range(token[0], token[1] + 1, token[2])])

        else:
            result.append(int(val))

    return result
