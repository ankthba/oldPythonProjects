input1 = '6, 8, 1, 5, 2, 3, 5, 3, 7, 9'
input2 = '7, 6, 2, 9'
input3 = '9, 3, 4, 6, 1, 8, 6, 4, 2, 8, 4'

list1 = input1.split(',')
list2 = input2.split(',')
list3 = input3.split(',')

len1 = len(list1)
len2 = len(list2)
len3 = len(list3)

max_len = max(len1, len2, len3)

sum_max_items = 0

for i in range(max_len):
  item1 = 0
  if(i < len1):
    item1 = int(list1[i])

  item2 = 0
  if(i < len2):
    item2 = int(list2[i])

  item3 = 0
  if(i < len3):
    item3 = int(list3[i])

  max_item = max(item1,item2,item3)

  sum_max_items = sum_max_items + max_item


print(sum_max_items)