import argparse
import string


parser = argparse.ArgumentParser()
parser.add_argument('file', help='Add path to the file')
args = parser.parse_args()
path = args.file
file = open(path)
words = file.read().split()
words_normalize = []
for word in words:
  words_lower = word.lower()
  words_punctuation = words_lower.translate(str.maketrans('', '', string.punctuation))
  words_whitespaces = words_punctuation.strip()  
  words_normalize.append(words_whitespaces)
  words_normalize.sort(key=len, reverse=True)
print(words_normalize[0], words_normalize[1], words_normalize[2])
