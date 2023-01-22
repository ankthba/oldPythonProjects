


def divide(user_input):
  if "DIVIDE" in user_input:
    first_4 = user_input[0:4]
    last_4 = user_input[4:]
    x = last_4, last_4

  return first_4 + first_4, 'and', last_4 + last_4
  '''else:
    return add()'''
  if "ADD" in user_input:
    return add(user_input)
#--------------------------------------------------------

def add(user_input):
  if "ADD" in user_input:
  #def add(user_input):
    y = user_input[3]


    cell = user_input[5:]
    stry = str(y)
    inty = int(stry)
    add = cell[inty]

    stry = str(user_input)

    print(str(user_input).split(5,1)[1])

  
    num1 = user_input[3]

    intnum1 = int(num1)


    splits1 = user_input.split()

    z1 = splits1[1]

    a1 = z1[0: intnum1]

    q1 = a1+a1

    return q1
  else:
    return subtract(user_input)

    

#--------------------------------------------------------

def subtract(expr):
  if "SUBTRACT" in expr:
    num = expr[8]

    intnum = int(num)


    splits = expr.split()

    z = splits[1]

    a = z[intnum:]

    return a+a
  else:
    return none

user_input = input("What is your input: ")
