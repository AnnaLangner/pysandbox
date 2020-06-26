#Script which will take as an input url to the page and text.
import argparse
import requests


parser = argparse.ArgumentParser()
parser.add_argument('--url', help='add url')
parser.add_argument('--text', help='add text')
args = parser.parse_args()
url = args.url
text = args.text
url = input('Enter the URL:')
text = input('Enter the search phrase: ')
r = requests.get(url)
if text in r.text:
  print(text)  
else:
  print("Text '" + text + "' not found")
