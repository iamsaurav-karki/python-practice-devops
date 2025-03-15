import sys

type = sys.argv[1]

if type == 't2.micro':
  print("okay , it will charge you 0.0116 USD per Hour!!")

elif type == 't2.small':
  print("okay , it will charge you 0.023 USD per Hour!!")

else:
  print("Invalid instance type")
  sys.exit(1)