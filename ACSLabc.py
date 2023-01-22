def get_filled_values(grid,pos,rows_columns):
  filled_list = []
  for pos_list in rows_columns:
    if pos in pos_list:
      for next_pos in pos_list:
        next_val = grid[str(next_pos)] 
        if next_val != 'X' and next_val not in filled_list:
          filled_list.append(next_val)
  return filled_list

def get_possible_values(grid, pos, rows_columns):
  filled_list = get_filled_values(grid,pos,rows_columns)
  possible_list = []
  for item in ['A','B','C']:
    if item not in filled_list:
      possible_list.append(item)
  
  return possible_list


#user_input = "3, 1, A, 3, C, 8, A"
user_input = input("Enter input: ")

rows_columns = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9]] 

grid_dict = {}
# fill the grid with X as a start
for num in range(1,10):
  grid_dict[str(num)] = 'X'

splits = user_input.split(',')
in_grid_ct = int(splits[0].strip())
grid_pairs = splits[1:]

# use inputs to pre-fill values. 
for pos in range(0,in_grid_ct):
  grid_num = grid_pairs[pos * 2].strip()
  grid_val = grid_pairs[pos * 2 + 1].strip()
  grid_dict[grid_num] = grid_val

# create a copy of the grid and work on the copy 
working_grid_dict = grid_dict.copy()
# try to assing values
completed = False
num_iterations = 0
while(completed == False):
  num_iterations = num_iterations + 1
  for pos in range(1,10):
    if working_grid_dict[str(pos)] == 'X':
      possible_values = get_possible_values(working_grid_dict, pos, rows_columns)
      #print("possible values for positon ",str(pos)," are ",possible_values)
      if len(possible_values) == 0:
        print("Error: no possible values for position ",str(pos))
      elif len(possible_values) == 1:
        working_grid_dict[str(pos)] = possible_values[0]
      #else:
      #  print(str(pos)," position is pushed to next iteration")

  #check if grid is filled
  completed = 'X' not in working_grid_dict.values()  

#print("num iterations: ", num_iterations)    
print(working_grid_dict)