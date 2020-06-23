import argparse
import re


parser = argparse.ArgumentParser()
parser.add_argument('file', help='Add path to the file')
args = parser.parse_args()
path = args.file
file = open(path)
#without regex & with replace()
# words = file.read().split()
# words_normalize = []
# for word in words:
#   words_lower = word.lower()
#   words_punctuation = words_lower.replace(",", " ").replace(".", " ").replace("-", "")
#   words_whitespaces = words_punctuation.strip()  
#   words_normalize.append(words_whitespaces)
# words_normalize.sort(key=len, reverse=True)
# print(words_normalize[0], words_normalize[1], words_normalize[2])
#
#with regex
words = file.read()
words = re.sub("\W", " ", words).lower().split()
words.sort(key=len, reverse=True)
print(words[0], words[1], words[2])
