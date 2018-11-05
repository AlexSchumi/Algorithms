print('Hello World')

matrix = [[]]
print(len(matrix))
if len(matrix) == 0:
    print('yes')
else:
    print('no')

print(len(matrix[0]))

#If you want different variable use slice operator:
#s1 = s[:]

a = [1,2,3]
b = a[:2]
a.pop(0)
print(a[0])
print(b[0])

for x in range(5,-1,-1):
    print(x)

a = []
a.append((1,2))
a += (3,4)
print(a)
print((1,2) in a)

count_dict, count = {}, 0

import numpy as np
nums = [2,3,4,5,6,1,2,3,3,3]
for num in nums:
    count_dict[num] = count_dict.get(num,0) + 1

#print(list(count_dict.values()) > 1)

import collections
c = collections.Counter(nums)
print(c)

def twoSum(nums, target):
    for i in range(len(nums)):
        print(i)
        if (target - nums[i]) in nums and nums.index(target-nums[i]) != i:
            return [i, nums.index(target - nums[i])]
    else:
        pass

print(twoSum([3,2,4],6))

a = 'abc'
a.split(' ')
print(list(a))

s = 'abcd'

for char in s:
    print(char)
dict = {"]":"[", "}":"{", ")":"("}

for val in dict.keys():
    print(val)

print(10//10)
s = ' '
memory = ''
memory += '1'
memory += 'a'
print(memory[1:])

nums = [3,4,-1,1]
nums.sort()
for i, num in enumerate(nums,1):
    print([i,num])


s = 'abba'
print(s[1:3] == s[1:3][::-1])
print(s[1:3])
print(list(s))
l1 = list(s)
l2 = l1
print(l2)
l2[0] = 'c'
test = [0, 1, 2, 3, 4]
print(test[5:])

matrix = [1,2,3]
print(matrix[1:3][::-1])

str = "dog dog dog dog"
str = str.split(' ')

wordDict = ["cats", "dog", "sand", "and", "cat"]
s = 'leetcode'
print(len(s))
s = ' ' + s
print(len(s))
print(s)
print(s in wordDict)

test = {}
test['a'] = 1
test['b'] = 4
test['c'] = 10
xx = ['a','z','c', 'b', 'b','a']
a = [1,2,3,4,5,5,5,5]
a.remove(5)
A = [ord(x) - ord('a') for x in xx]
test_a = 'abc'
print(4562 / 10 % 10)
