# leetcode python

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]


solution = Solution()

solution.twoSum([1, 2, 3, 4, 5, 6, 7, 8, 9], 9)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):


200//10

200 % 10

x = 123

print(str(x))

print(str(x)[::-1])

str(x)[::-3]


'good morning'[1::-1]
