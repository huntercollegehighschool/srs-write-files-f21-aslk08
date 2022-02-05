import shelve

option = input("Enter A or B or M: ").lower()

while option not in 'amb':
  print("That's not valid.")
  option = input("Enter A or B or M: ")

if option == 'a':
  import ASavetodb

elif option == 'b':
  import BQuizzes

elif option == 'm':
  import MQuizzes