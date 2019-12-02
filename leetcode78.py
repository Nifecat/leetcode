from typing import List


class Solution:
    def __init__(self):
        self.res = None
    def subsets(self, nums: List[int]) -> List[List[int]]:

          item=[]
          self.res=[]
          self.res.append(item)
          self.generate(0, nums, item)
          return self.res

    def generate(self,i,nums,item):
        if i>=len(nums):
            return
        item.append(nums[i])
        ta = []
        ta.extend(item)
        self.res.append(ta)
        print(self.res)
        self.generate(i+1,nums,item)
        item.pop()
        self.generate(i+1,nums,item)






if __name__ == '__main__':
    s=Solution()
    nums=[1,2,3]
    res=s.subsets(nums)
    print(res)