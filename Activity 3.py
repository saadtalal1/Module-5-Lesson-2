num_sum=int(input("Enter the num that you want the sum to add to: "))
nums=[10,20,30,40,50,60,70]
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==num_sum:
            print(nums[i],nums[j])
    
        
