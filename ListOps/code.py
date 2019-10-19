'''
Task: Delete alternate elements of the given list, starting from index 0,
      print the list after each traversal.

Example: given list -> [1,2,3,4,5]
                o/p: [2, 4]
                     [4]
                     []

'''

nums = [3, 5, 2, 9, 101, 333, 4]
nums_1=[]
while(len(nums) !=0):
 for i in range(0,len(nums)):
      if(i%2==0):
            nums_1.append(i)
      print(nums_1)

