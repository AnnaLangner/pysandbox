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
  for m in re.finditer(text, r.text):
    start = m.start()
    end = m.end()
    new_text = r.text[start-10:end+10]
    print(new_text)
args = arguments()
url = args.url
text = args.text
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
