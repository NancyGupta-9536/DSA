nums=[6,7,7,8,9,3,4]
hash_map=dict()
n=len(nums)
for i in range(0,n):
 hash_map[nums[i]]=hash_map.get(nums[i],0)+1
print(hash_map[7])