#Script which will take as an input url to the page and text.
import argparse
import requests
import re


def arguments():
  parser = argparse.ArgumentParser()
  parser.add_argument('--url', help='add url')
  parser.add_argument('--text', help='add text')
  args = parser.parse_args()
  return args
def add_characters():
  length_text = len(text)
  start = r.text.index(text)
  new_text.append(r.text[start:10+start])
  new_text.append(r.text[start:start+(length_text+10)])    
  print(''.join(new_text))
args = arguments()
url = args.url
text = args.text
new_text = []
r = requests.get(url)
if args:
  if text in r.text:
    add_characters()
  else:
    print("Text '" + text + "' not found")
else:
  url = input('Enter the URL:')
  text = input('Enter the search phrase: ')
  if text in r.text:
    add_characters()
  else:
    print("Text '" + text + "' not found")
