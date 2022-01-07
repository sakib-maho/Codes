jewels = 'aA'
stones = 'aAAbbbb'
total = 0
result = "".join(dict.fromkeys(jewels))

for i in result:
    total = total + stones.count(i)

print(total)
