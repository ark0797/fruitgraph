import argparse
import sys

parser = argparse.ArgumentParser(
    description='Kyrilic'
)

parser.add_argument(
    'values',
    metavar='VALUES',
    type=float,
    nargs=2,
    help='input'
)

parser.add_argument(
    '-a',
    '--action',
    action = 'store',
    metavar = "Symbol",
    help = 'nana'
)
args = parser.parse_args()
val = args.values
if args.action == "+":
    print(val[0]+val[1])
elif args.action == "-":
    print(val[0]-val[1])
elif args.action == "*":
    print(val[0]*val[1])
elif args.action == "/":
    print(val[0]/val[1])
else:
    print("Некоректная операция")
