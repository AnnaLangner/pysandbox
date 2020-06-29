#Script which will take as an input url to the page and text.
import argparse
import requests
import re


def fetch_arguments():
  parser = argparse.ArgumentParser()
  parser.add_argument('--url', help='add url')
  parser.add_argument('--text', help='add text')
  args = parser.parse_args() 
  return args


def print_10_characters_before_and_after_text():
  for m in re.finditer(text, r.text):
    start = m.start()
    end = m.end()
    new_text = r.text[start-10:end+10]
    return new_text


try:
  args = fetch_arguments()
  url = args.url
  text = args.text
  r = requests.get(url) 
  if text in r.text:
    print(print_10_characters_before_and_after_text())
  else:
    print("Text '" + text + "' not found")  
except:
  print("Error: This code works when enter the url and text.")  
