# Sliding window problem to get max sum of kth elements in the array
def maxSum(arr,n,k):
    if not n > k:
        print("Invalid input")
        return -1

    max_sum = window_sum = sum([arr[i] for i in range(k)])

    for i in range(n-k):
        window_sum = window_sum - arr[i] + arr[k+i]
        max_sum = max(window_sum,max_sum)

    return max_sum

arr = [-1,-2,-3,-4,-5]
k = 3
n = len(arr)
print(maxSum(arr,n,k))
 
    