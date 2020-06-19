import argparse


parser = argparse.ArgumentParser()
parser.add_argument('fruit', nargs='*')
args = parser.parse_args()
sort_list = sorted(args.fruit)
#the first way
#print(*sort_list, sep=', ')
#the second way
fruits = ", ".join(sort_list)
print(fruits)
