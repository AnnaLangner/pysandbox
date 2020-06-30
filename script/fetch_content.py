#Script which will take as an input url to the page and text.
import argparse
import requests
import re


def fetch_arguments():
  """Fetch arguments from command line"""

  parser = argparse.ArgumentParser()
  parser.add_argument('url', help='add url')
  parser.add_argument('text', help='add text')
  args = parser.parse_args()  
  return (args.url, args.text)


def print_10_characters_before_and_after_text(text, r):
  """
  Print text with  additional characters.

  This function retrieves the text and returns it with an additional ten characters before and after the text.

  parameters:
  text: text that someone enters
  r.text: all text on the website
  start: index of the first letter of the entered text
  end: index of the last letter of the entered text
  new_text: a string with additional characters added before start and after end.

  Return:
  string: text with 10 additional characters before and after.
  
  """

  for m in re.finditer(text, r.text):
    start = m.start()
    end = m.end()
    new_text = r.text[start-10:end+10]
    return new_text.split(text, 2)


try:
  (url, text) = fetch_arguments()
  r = requests.get(url) 
  if text in r.text:
    print(print_10_characters_before_and_after_text(text, r))
  else:
    print("Text '" + text + "' not found")  
except:
  print("Error: This code works when enter the url and text.")  
