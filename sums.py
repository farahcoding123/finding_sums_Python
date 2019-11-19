def sum(nums,sums):
    for num in nums:
        missing = sums - num
        if missing in nums:
            return [num,missing]

    return []


print(sum([1,2,4,-1,25],27))
