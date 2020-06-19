import argparse


parser = argparse.ArgumentParser()
parser.add_argument('fruit', nargs='*')
args = parser.parse_args()
sort_list = sorted(args.fruit)
print(*sort_list, sep=', ')
