import argparse


parser = argparse.ArgumentParser()
parser.add_argument('fruit', nargs='*')
args = parser.parse_args()
sortList = sorted(args.fruit)
for i in sortList:
  print(i)
