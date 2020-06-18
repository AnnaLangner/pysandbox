import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--name", help="name the string you are use here")
args = parser.parse_args()
if args.name:
  print('Hello', args.name)
else:
 args.name = input('Whats Your name?')
  print('Hello', args.name)
  