# Copyright (c) 2025 sakib-maho
# Licensed under the MIT License
# See LICENSE file for details

jewels = 'aA'
stones = 'aAAbbbb'
total = 0
result = "".join(dict.fromkeys(jewels))

for i in result:
    total = total + stones.count(i)

print(total)
