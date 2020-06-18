#This script should take 2 parameters (numbers) and print lower number on the console.
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("num1", help="num is the int you use here")
parser.add_argument("num2", help="num is the int you use here")
args = parser.parse_args()
if float(args.num1) > float(args.num2): 
  print("Lower number:", args.num2)
elif float(args.num1) < float(args.num2):
  print("Lower number:", args.num1)
else:
  print("Numbers are equal")
  