def findMaxAverage(nums,k):
    s = sum(nums[:k])
    output = [sum(nums[:k])]
    for i in range(1,len(nums)-k+1):
        s = s-nums[i-1]+nums[i-1+k]
        output.append(s)

    return max(output)/k