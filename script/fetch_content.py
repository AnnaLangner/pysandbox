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
  Print text with additional characters.

  This function retrieves the text and returns it with an additional ten characters before and after the text. If no text is found, it returns an empty string.

  Parameters:
  search_phrase: text that someone enters.
  r.text: all text on the website.
  first_occurrence: first occurrence of the search phrase.
  start: index of the first letter of the entered text.
  end: index of the last letter of the entered text.
  new_text: a string with additional characters added before start and after end. 

  Return:
  new_text
  """ 
  

  first_occurrence = r.text.find(search_phrase)
  if first_occurrence >= 0:
    start = first_occurrence
    end = first_occurrence + len(search_phrase)
    new_text = r.text[start-10:end+10]
    return new_text
  else:
    return ""


(url, search_phrase) = fetch_arguments()
r = requests.get(url) 
result = print_10_characters_before_and_after_text(search_phrase, r.text)
if len(result) == 0:
  print("Text '" + search_phrase + "' not found")
else:
  print(result)
