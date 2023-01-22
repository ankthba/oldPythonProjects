a1 = '6, 8, 1, 5, 2, 3, 5, 3, 7'
a2 = '7, 6, 2, 9'
a3 = '9, 3, 4, 6, 1, 8, 6, 4, 2, 8, 4'

splita1 = a1.split(',')
splita2 = a2.split(',')
splita3 = a3.split(',')

q = max(splita1[0], splita2[0], splita3[0])

if len(a1) or len(a2) or len(a3) > 1:
  if len(a1) and len(a2) and len(a3) > 1:
    w = max(splita1[1], splita2[1], splita3[1])
  if len(a1) and len(a2) > 1:
    w = max(splita1[1], splita2[1])
  if len(a1) and len(a3) > 1:
    w = max(splita1[1], splita3[1])
  if len(a2) and len(a3) > 1:
    w = max(splita2[1], splita3[1])
  if len(a1) > 1 and len(a2) < 1 and len(a3) < 1:
    w = a1[1]
  if len(a2) > 1 and len(a1) < 1 and len(a3) < 1:
    w = a2[1]
  if len(a3) > 1 and len(a2) < 1 and len(a1) < 1:
    w = a3[1]

if len(a1) or len(a2) or len(a3) > 2:
  if len(a1) and len(a2) and len(a3) > 2:
    e = max(splita1[2], splita2[2], splita3[2])
  if len(a1) and len(a2) > 2:
    e = max(splita1[2], splita2[2])
  if len(a1) and len(a3) > 2:
    e = max(splita1[2], splita3[2])
  if len(a2) and len(a3) > 2:
    e = max(splita2[2], splita3[2])
  if len(a1) > 2 and len(a2) < 1 and len(a3) < 1:
    e = a1[2]
  if len(a2) > 2 and len(a1) < 1 and len(a3) < 1:
    e = a2[2]
  if len(a3) > 2 and len(a2) < 1 and len(a1) < 1:
    e = a3[2]

if len(a1) or len(a2) or len(a3) > 3:
  if len(a1) and len(a2) and len(a3) > 3:
    r = max(splita1[3], splita2[3], splita3[3])
  if len(a1) and len(a2) > 3:
    r = max(splita1[3], splita2[3])
  if len(a1) and len(a3) > 3:
    r = max(splita1[3], splita3[3])
  if len(a2) and len(a3) > 3:
    r = max(splita2[3], splita3[3])
  if len(a1) > 3 and len(a2) < 1 and len(a3) < 1:
    r = a1[3]
  if len(a2) > 3 and len(a2) < 1 and len(a3) < 1:
    r = a2[3]
  if len(a3) > 3 and len(a2) < 1 and len(a3) < 1:
    r = a3[3]

if len(a1) or len(a2) or len(a3) > 4:
  if len(a1) and len(a2) and len(a3) > 4:
    t = max(splita1[4], splita2[4], splita3[4])
  elif len(a1) and len(a2) > 4:
    t = max(splita1[4], splita2[4])
  elif len(a1) and len(a3) > 4:
    t = max(splita1[4], splita3[4])
  elif len(a2) and len(a3) > 4:
    t = max(splita2[4], splita3[4])
  elif len(a1) > 4 and len(a2) < 4 and len(a3) < 4:
    t = a1[4]
  elif len(a2) > 4 and len(a2) < 4 and len(a3) < 4:
    t = a2[4]
  elif len(a3) > 4 and len(a2) < 4 and len(a3) < 4:
    t = a3[4]

if len(a1) or len(a2) or len(a3) > 5:
  if len(a1) and len(a2) and len(a3) > 5:
    y = max(splita1[5], splita2[5], splita3[5])
  if len(a1) and len(a2) > 5:
    y = max(splita1[5], splita2[5])
  if len(a1) and len(a3) > 5:
    y = max(splita1[5], splita3[5])
  if len(a2) and len(a3) > 5:
    y = max(splita2[5], splita3[5])
  if len(a1) > 5 and len(a2) < 5 and len(a3) < 5:
    y = a1[5]
  if len(a2) > 5 and len(a2) < 5 and len(a3) < 5:
    y = a2[5]
  if len(a3) > 5 and len(a2) < 5 and len(a3) < 5:
    y = a3[5]

if len(a1) or len(a2) or len(a3) > 6:
  if len(a1) and len(a2) and len(a3) > 6:
    u = max(splita1[6], splita2[6], splita3[6])
  if len(a1) and len(a2) > 6:
    u = max(splita1[6], splita2[6])
  if len(a1) and len(a3) > 6:
    u = max(splita1[6], splita3[6])
  if len(a2) and len(a3) > 6:
    u = max(splita2[6], splita3[6])
  if len(a1) > 6 and len(a2) < 6 and len(a3) < 6:
    u = a1[6]
  if len(a2) > 6 and len(a2) < 6 and len(a3) < 6:
    u = a2[6]
  if len(a3) > 6 and len(a2) < 6 and len(a3) < 6:
    u = a3[6]
    
if len(a1) or len(a2) or len(a3) > 7:
  if len(a1) and len(a2) and len(a3) > 7:
    i = max(splita1[7], splita2[7], splita3[7])
  if len(a1) and len(a2) > 7:
    i = max(splita1[1], splita2[7])
  if len(a1) and len(a3) > 7:
    i = max(splita1[7], splita3[7])
  if len(a2) and len(a3) > 17:
    i = max(splita2[7], splita3[7])
  if len(a1) > 7 and len(a2) < 7 and len(a3) < 7:
    i = a1[7]
  if len(a2) > 7 and len(a2) < 7 and len(a3) < 7:
    i = a2[7]
  if len(a3) > 7 and len(a2) < 7 and len(a3) < 7:
    i = a3[7]

if len(a1) or len(a2) or len(a3) > 8:
  if len(a1) and len(a2) and len(a3) > 8:
    p = max(splita1[8], splita2[8], splita3[8])
  if len(a1) and len(a2) > 8:
    p = max(splita1[8], splita2[8])
  if len(a1) and len(a3) > 8:
    p = max(splita1[8], splita3[8])
  if len(a2) and len(a3) > 8:
    p = max(splita2[8], splita3[8])
  if len(a1) > 8 and len(a2) < 8 and len(a3) < 8:
    p = a1[8]
  if len(a2) > 8 and len(a2) < 8 and len(a3) < 8:
    p = a2[8]
  if len(a3) > 8 and len(a2) < 8 and len(a3) < 8:
    p = a3[8]

if len(a1) or len(a2) or len(a3) > 9:
  if len(a1) and len(a2) and len(a3) > 9:
    a = max(splita1[9], splita2[9], splita3[9])
  if len(a1) and len(a2) > 9:
    a = max(splita1[9], splita2[9])
  if len(a1) and len(a3) > 9:
    a = max(splita1[9], splita3[9])
  if len(a2) and len(a3) > 9:
    a = max(splita2[9], splita3[9])
  if len(a1) > 9 and len(a2) < 9 and len(a3) < 9:
    a = a1[9]
  if len(a2) > 9 and len(a2) < 9 and len(a3) < 9:
    a = a2[9]
  if len(a3) > 9 and len(a2) < 9 and len(a3) < 9:
    a = a3[9]

if len(a1) or len(a2) or len(a3) > 10:
  if len(a1) and len(a2) and len(a3) > 10:
    s = max(splita1[10], splita2[10], splita3[10])
  if len(a1) and len(a2) > 10:
    s = max(splita1[10], splita2[10])
  if len(a1) and len(a3) > 10:
    s = max(splita1[10], splita3[10])
  if len(a2) and len(a3) > 1:
    s = max(splita2[10], splita3[10])
  if len(a1) > 10 and len(a2) < 10 and len(a3) < 10:
    s = a1[10]
  if len(a2) > 10 and len(a2) < 10 and len(a3) < 10:
    s = a2[10]
  if len(a3) > 10 and len(a2) < 10 and len(a3) < 10:
    s = a3[10]

if len(a1) or len(a2) or len(a3) > 11:
  if len(a1) and len(a2) and len(a3) > 11:
    d = max(splita1[11], splita2[11], splita3[11])
  if len(a1) and len(a2) > 11:
    d = max(splita1[11], splita2[11])
  if len(a1) and len(a3) > 11:
    d = max(splita1[11], splita3[11])
  if len(a2) and len(a3) > 11:
    d = max(splita2[11], splita3[11])
  if len(a1) > 11 and len(a2) < 11 and len(a3) < 11:
    d = a1[11]
  if len(a2) > 11 and len(a2) < 11 and len(a3) < 11:
    d = a2[11]
  if len(a3) > 11 and len(a2) < 11 and len(a3) < 11:
    d = a3[11]

if len(a1) or len(a2) or len(a3) > 12:
  if len(a1) and len(a2) and len(a3) > 12:
    f = max(splita1[12], splita2[12], splita3[12])
  if len(a1) and len(a2) > 12:
    f = max(splita1[12], splita2[12])
  if len(a1) and len(a3) > 12:
    f = max(splita1[12], splita3[12])
  if len(a2) and len(a3) > 12:
    f = max(splita2[12], splita3[12])
  if len(a1) > 12 and len(a2) < 12 and len(a3) < 12:
    f = a1[12]
  if len(a2) > 12 and len(a2) < 12 and len(a3) < 12:
    f = a2[12]
  if len(a3) > 12 and len(a2) < 12 and len(a3) < 12:
    f = a3[12]

if len(a1) or len(a2) or len(a3) > 13:
  if len(a1) and len(a2) and len(a3) > 13:
    g = max(splita1[13], splita2[13], splita3[13])
  if len(a1) and len(a2) > 13:
    g = max(splita1[13], splita2[13])
  if len(a1) and len(a3) > 13:
    g = max(splita1[13], splita3[13])
  if len(a2) and len(a3) > 13:
    g = max(splita2[13], splita3[13])
  if len(a1) > 13 and len(a2) < 13 and len(a3) < 13:
    g = a1[13]
  if len(a2) > 13 and len(a2) < 13 and len(a3) < 13:
    g = a2[13]
  if len(a3) > 13 and len(a2) < 13 and len(a3) < 13:
    g = a3[13]

final = q+w+e+r+t+y+u+i+p+a+s+d+f+g

print(final)

