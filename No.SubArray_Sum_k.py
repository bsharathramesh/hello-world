# Number of consecutive sub array such that sum = k 
from collections import defaultdict
def subArraySum(arr,k):
    ht = defaultdict(int)
    sum = 0
    count = 0
    ht[0] = 1
    for i in arr:
        sum += i
        count = count + ht[sum-k]
        ht[sum] = ht[sum] + 1
    return count

arr = [1,1,1,1]
output = subArraySum(arr,3)
print(output)