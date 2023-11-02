import re

player = input().split(",")
print(player)
pattern = '^\w+\s+\w+$'

for name in player:
    match = re.match(pattern, name)
    if match:
        last_name = name.split()[-1]
        print(last_name)
