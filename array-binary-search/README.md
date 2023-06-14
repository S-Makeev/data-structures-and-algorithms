# Challenge Title
<!-- Description of the challenge -->
array-binary-search

## Whiteboard Process
<!-- Embedded whiteboard image -->
[array-binary-search](array-binary-search.png)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
Time O(n)
Space O(log n)

## Solution
<!-- Show how to run your code, and examples of it in action -->

def BinarySearch(arr, key):
low = 0
high = len(list)-1
while low <= high:
  mid = (low + high) // 2
  if arr[mid] == key
    return mid
  elif: arr[mid] < key
    low = mid + 1
  else:
    high = mid -1
return -1
