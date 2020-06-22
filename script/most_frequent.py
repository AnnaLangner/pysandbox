import argparse
from collections import Counter 


parser = argparse.ArgumentParser()
parser.add_argument('file', help='Add path to the file')
args = parser.parse_args()
path = args.file
file = open(path)
words = file.read().split()
frequenty_words = Counter(words).most_common(3)
for word in frequenty_words:
  #tuples
  #print(word[0], ":", word[1])
  #string interpolation:
  print(f'{word[0]} : {word[1]}')
