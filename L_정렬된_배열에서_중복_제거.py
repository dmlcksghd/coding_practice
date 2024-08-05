def remove_duplicates(num):
    num = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            num.append(nums[i])
    return num