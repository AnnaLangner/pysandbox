#Script which will take as an input url to the page and text.
import argparse
import requests
import re


def fetch_arguments():
  """Fetch arguments from command line"""

  parser = argparse.ArgumentParser()
  parser.add_argument('url', help='add url')
  parser.add_argument('search_phrase', help='add text')
  args = parser.parse_args()  
  return (args.url, args.search_phrase)


def print_10_characters_before_and_after_text(search_phrase, text):
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
   
  if search_phrase in r.text:
    for m in re.finditer(search_phrase, r.text):
      start = m.start()
      end = m.end()
      new_text = r.text[start-10:end+10]
      return new_text
  else:
    print("Text '" + search_phrase + "' not found") 


try:
  (url, search_phrase) = fetch_arguments()
  r = requests.get(url) 
  print(print_10_characters_before_and_after_text(search_phrase, r.text).split(search_phrase, 2))
except:
  print("Error: This code works when enter the url and text.")  
