import argparse
import requests


parser = argparse.ArgumentParser()
parser.add_argument('url', help='Add url')
args = parser.parse_args()
url = args.url
r = requests.get(url)
print('Status code:', r.status_code)
