nums=[5,6,7,7,8,9,3,1,8,9]
freq_map=dict()
for i in range(0,len(nums)):
    if(nums[i]in freq_map):
        freq_map[nums[i]]+=1
    else:
        freq_map[nums[i]]=1
print(freq_map[5])