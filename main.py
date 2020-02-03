from argparse import ArgumentParser
from functions import prod

def calc():
    print(oper(numbers))

def parser():
    parser = ArgumentParser(description="Calculator")
    parser.add_argument("numbers", type= int, nargs="+")
    group = parser.add_mutually_exclusive_group(required=True)
    parser.add_argument("-sum", action='store_const', const=sum)
    parser.add_argument("-prod", action='store_const', const=prod)
    parser.add_argument("-reverse",action='store_true')
    args = parser.parse_args()
    list_nnumber = args.numbers
    operation = args.oper
    reverse = args.reverse
    return list_numbers, operation, reverse

if __name__ = "__main__":
    numbers, oper, rev = parser()
    res = calc(numbers,oper)

    if rev:
        print(str(res)[::-1])
    else:
        print(str(res))

'''
parser = ArgumentParser(description="Aquí la descripción")

parser.add_argument("topdown", metavar="T", type= str, nargs=1,2..., help = "mensaje ayuda")
args = parser.parse_args()

string = args["Nombre variable"]
'''