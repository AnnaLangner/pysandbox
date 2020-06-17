import argparse
parser = argparse.ArgumentParser()
parser.add_argument("name", help="name the string you are use here")
args = parser.parse_args()
print('Hello', args.name)