
user_input = input("What is your input: ")


if "DIVIDE" in user_input:
  splits = user_input.split()
  term = splits[1]
  first_4 = term[:4]
  last_4 = term[4:]
  x = last_4, last_4

  print(first_4 + first_4,'and', last_4 + last_4) 
  
  
#--------------------------------------------------------

if "ADD" in user_input:
#def add(user_input):
  y = user_input[3]

  cell = user_input[5:]
  stry = str(y)
  inty = int(stry)
  add = cell[inty]
  stry = str(user_input)
  print(str(user_input).split('5',1)[0])

  num1 = user_input[3]

  intnum1 = int(num1)


  splits1 = user_input.split()

  z1 = splits1[1]

  a1 = z1[0: intnum1]

  q1 = a1+a1

  print(q1)

    

#--------------------------------------------------------


if "SUBTRACT" in user_input:
  num = user_input[8]

  intnum = int(num)


  splits = user_input.split()

  z = splits[1]

  a = z[intnum:]

  print(a+a)



