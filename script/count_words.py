import argparse


parser = argparse.ArgumentParser()
parser.add_argument("file", help="Entry a path to the file")
args = parser.parse_args()
path = args.file
file = open(path)
words = file.read().split()
print(len(words))
