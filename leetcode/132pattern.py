# Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

# Return true if there is a 132 pattern in nums, otherwise, return false.


from mimetypes import init
from unicodedata import name

def find132pattern(nums: list[int]) -> bool:
    stack=[] # pair [num,minLeft], monotonically decreasing
    curMin = nums[0]
    for n in nums[1:]:
        while stack and n>=stack[-1][0]:
            stack.pop()
        if stack and n> stack[-1][1]:
            return True
        stack.append([n,curMin])
        curMin = min(curMin, n)
    return False
    
if __name__ == "__main__" :
    nums=[3,1,4,2]
    print("Eg : ",nums," = ",find132pattern(nums))
    n=int(input("Enter the length"))
    k=[0]*n
    for i in range(n):
        k[i]=int(input())
    print(k," = ",find132pattern(k))


