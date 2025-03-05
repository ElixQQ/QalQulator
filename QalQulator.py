print("""
  ___        _  ___        _       _             
 / _ \  __ _| |/ _ \ _   _| | __ _| |_ ___  _ __ 
| | | |/ _` | | | | | | | | |/ _` | __/ _ \| '__|
| |_| | (_| | | |_| | |_| | | (_| | || (_) | |   
 \__\_\\__,_|_|\__\_\\__,_|_|\__,_|\__\___/|_|   
""")

loop = True

while loop == True:

  firstInput = int(input("First input: "))
  secondInput = int(input("Second input: "))

  operator = int(input("""\nOperator:\n1.Plus\n2.Minus\n3.Multi\n4.Subs\n\nInput: """))



  if operator == 1:
    print(firstInput+secondInput)
    againInput = int(input("\n1.Again\n2.Exit\n"))
    if againInput == 1:
      loop == True
    elif againInput == 2:
      loop = False

  elif operator == 2:
    print(firstInput-secondInput)
    againInput = int(input("\n1.Again\n2.Exit\n"))
    if againInput == 1:
      loop == True
    elif againInput == 2:
      loop = False
    
  elif operator == 3:
    print(firstInput*secondInput)
    againInput = int(input("\n1.Again\n2.Exit\n"))
    if againInput == 1:
      loop == True
    elif againInput == 2:
      loop = False

  elif operator == 4:
    print(firstInput/secondInput)
    againInput = int(input("\n1.Again\n2.Exit\n"))
    if againInput == 1:
      loop == True
    elif againInput == 2:
      loop = False

  else:
    print("Wrong input")
    againInput = int(input("\n1.Again\n2.Exit\n"))
    if againInput == 1:
      loop == True
    elif againInput == 2:
      loop = False