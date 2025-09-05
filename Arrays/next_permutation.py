# Day 5 – Next Permutation

## 📌 Problem Statement
'''The task is to rearrange numbers into the lexicographically next greater permutation of numbers.  
If such arrangement is not possible (i.e., array is in descending order), rearrange it as the lowest possible order (ascending).

- Example:
  - Input: [1, 2, 3]
  - Output: [1, 3, 2]

## 📝 Explanation
- We need to find the next permutation in dictionary order.
- Steps:
  1. Find the first index `i` from the right such that `nums[i] < nums[i+1]`.
  2. Find the first index `j` from the right such that `nums[j] > nums[i]`.
  3. Swap `nums[i]` and `nums[j]`.
  4. Reverse the subarray from `i+1` to end.

This ensures the permutation is the immediate next larger one.

## 💡 My Notes
- This problem is a good exercise in array manipulation and understanding lexicographic ordering.
- Time complexity: **O(N)**.
- Space complexity: **O(1)** (in-place).

## 🧑‍💻 Solution (Python)
```python'''
class Solution:
    def nextPermutation(self, arr):
        n=len(arr)
        i=n-2
        while i>=0 and arr[i]>=arr[i+1]:
            i-=1
        if i>=0:
            j=n-1
            while arr[j]<=arr[i]:
                j-=1
            arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j=n-1
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        return arr
