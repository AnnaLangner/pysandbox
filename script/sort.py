import argparse


parser = argparse.ArgumentParser()
parser.add_argument('fruit', nargs='*')
args = parser.parse_args()
sortList = sorted(args.fruit)
print(*sortList, sep=', ')
