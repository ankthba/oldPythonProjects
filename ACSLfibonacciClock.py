def findTime(c1, c2, c3, c4, c5):
  hour_list = []

  if c1 == "R" or c1 == "B":
    hour_list.append(1)

  if c2 == "R" or c2 == "B":
    hour_list.append(1)

  if c3 == "R" or c3 == "B":
    hour_list. append (2)

  if c4 == "R" or c4 == "B":
    hour_list.append(3)

  if c5 == "R" or c5 == "B":
    hour_list.append(5)

  hours = sum(hour_list)

  minute_list = []

  if c1 == "G" or c1 == "B":
    minute_list.append(1)

  if c2 == "G" or c2 == "B":
    minute_list.append(1)

  if c3 == "G" or c3 == "B":
    minute_list.append(2)

  if c4 == "G" or c4 == "B":
    minute_list.append(3)

  if c5 == "G" or c5 == "B":
    minute_list.append(1)

  minutes = (sum((minute_list))*5)

  if hours < 10 and minutes > 9:
    return (f"0{hours}:{minutes}")
  elif hours > 9 and minutes > 9:
    return (f"{hours}:{minutes}")
  elif hours > 9 and minutes < 10:
    return (f"{hours}:0{minutes}")
  elif hours < 10 and minutes < 10:
    return (f"0{hours}:0{minutes}")
