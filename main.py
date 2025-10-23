# Copyright (c) 2025 sakib-maho
# Licensed under the MIT License
# See LICENSE file for details

nums = [3, 2, 4]
target = 6

for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            print(f'[{i}, {j}]')
            print(nums[i], nums[j])
            print(nums)
            break

    # if nums[i] + nums[i+1] == target:
    #     print(f'[{i}, {i+1}]')
    #     break
