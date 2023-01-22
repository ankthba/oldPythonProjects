user_input = "40, 42, 41, 49, 0"

splits = []
for inputs in user_input.split(","):
  splits.append(inputs.strip())

user1 = splits[0]
user2 = splits[1]

splits = splits[:-1]


grid = {}
for num in range(1,50):
  grid[str(num)] = "open"

for split in splits:
  grid[split] = "closed"

#print(grid)

#print("start:", user2)

start = int(user2)

# up list
uplist = []
up = start + 7
while(up < 50):
  if(grid[str(up)] == "open"):
    uplist.append(str(up))
    up = up + 7
  else:
    break

#print("uplist: ",uplist)

# down list
downlist = []
down = start - 7
while(down > 0):
  if(grid[str(down)] == "open"):
    downlist.append(str(down))
    down = down - 7
  else:
    break
  
#print("downlist: ",downlist)

# right list 
rightlist = []

max_in_row = 0
for multiple in range(1,8):
  if(7 * multiple >= start):
    max_in_row = 7 * multiple
    break

right = start + 1

while(right <= max_in_row):
  if(grid[str(right)] == "open"):
    rightlist.append(str(right))
    right = right + 1
  else:
    break
#print("rightlist",rightlist)

#left list
leftlist = []
left = start - 1

min_in_row = 50
for multiple in range(6,-1,-1):
  if((7 * multiple + 1) <= start):
    min_in_row = 7 * multiple + 1
    break

while(left >= min_in_row):
  if(grid[str(left)] == "open"):
    leftlist.append(str(left))
    left = left - 1
  else:
    break
#print("leftlist: ",leftlist)

largelist = []
for nextlist in [uplist,downlist,rightlist,leftlist]:
  if(len(nextlist) > len(largelist)):
    largelist = nextlist

print(largelist)