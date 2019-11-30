def largestSum(values, n):
    if n > len(values):
        return -1
    max_ = sum(values[0::n])
    for i in range(1, len(values)):
        max_ = max(sum(values[i::n]), max_)
    return max_
