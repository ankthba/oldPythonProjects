'''import re

# input
user_input = '2 COMPUTER bat'

# print(user_input)

# take away non-alphanumeric characters
letters = re.sub(r'[^a-zA-Z]', "", user_input)

# print(letters)

upperLetter = letters.upper()

print(upperLetter)'''

user_input = '2 COMPUTER bat'

splits = user_input.split(' ')
# print(splits)

mainString = list(splits[1])

addString = list(splits[2])

addition = mainString + addString

# print(addition)

sortedliststringthing = sorted(addition)

# print(sortedliststringthing)

joined = str(''.join(sortedliststringthing))

# print(joined)

print(len(joined))

caps = joined.upper()

semifinal = ''.join(sorted(caps))