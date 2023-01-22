input1 = '6 8 1 5 2 3 5 3 7 9'
input2 = '7 6 2 9'
input3 = '9 3 4 6 1 8 6 4 2 8 -1'

list1 = input1.strip().split(' ')
list2 = input2.strip().split(' ')
list3 = input3.strip().split(' ')

len1 = len(list1)
len2 = len(list2)
len3 = len(list3)

max_len = max(len1, len2, len3)

sum_max_items = 0

for i in range(max_len):
  pos_list = []
  if i < len1:
    pos_list.append(int(list1[i]))

  if i < len2:
    pos_list.append(int(list2[i]))

  if i < len3:
    pos_list.append(int(list3[i]))

  max_item = max(pos_list)

  sum_max_items = sum_max_items + max_item


print(sum_max_items)