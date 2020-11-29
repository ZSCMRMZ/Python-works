import time
start_time = time.time()

nums2 = [50, 20, 99, 4, 0, 23, 19]
def bucketSort(nums):
    max_num = max(nums)
    bucket = [0] * (max_num + 1)

    for i in nums:
        bucket[i] += 1

    sort_nums = []

    for j in range(len(bucket)):
        if bucket[j] != 0:
            for k in range (bucket[j]):
                sort_nums.append(j)
    return sort_nums
print(bucketSort(nums2))

end_time = time.time()
running_time = end_time - start_time
print(running_time)
input()
