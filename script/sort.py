import argparse


parser = argparse.ArgumentParser()
parser.add_argument('fruit', nargs='*')
args = parser.parse_args()
print("Sorted list:", sorted(args.fruit))
