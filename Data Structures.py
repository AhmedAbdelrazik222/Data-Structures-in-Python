def first_last6(nums):
  if nums[0] == 6 or nums[len(nums) - 1] == 6:
    return True
  else:
    return False

def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[len(nums) -1]:
    return True
  else:
    return False

def make_pi():
    make_pi=[3, 1, 4]
    return make_pi
  
def common_end(a, b):
  if a[0] == b[0] or a[len(a) -1] == b[len(b) -1]:
    return True
  else: 
    return False

def sum3(nums):
  return nums[0] + nums[1] + nums[2]

def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]

def reverse3(nums):
  return [nums[2], nums[1], nums[0]]

def max_end3(nums):
  if nums[0] > nums[2]:
    return [nums[0], nums[0], nums[0]]
  else:
    return [nums[2], nums[2], nums[2]]
  
def sum2(nums):
  if len(nums) >= 2:
    return nums[0] +nums[1]
  elif len(nums) == 1:
    return nums[0]
  else:
    return 0
  
def middle_way(a, b):
  return [a[1], b[1]]

def make_ends(nums):
  return [nums[0], nums[len(nums) -1]]

def has23(nums):
  if nums[0] == 2 or nums[0] == 3:
    return True
  elif nums[1] == 2 or nums[1] == 3:
    return True
  else: 
    return False

def count_evens(nums):
  count = 0
  for num in nums:
    if num % 2 == 0:
      count = count + 1
  return count

def big_diff(nums):
  max = nums[0]
  min = nums[0]
  for num in nums:
    if num >= max:
      max = num 
    elif num <= min:     
      min = num
  return max - min

def has22(nums):
    for i in range(len(nums)-1):
        if nums[i] == 2 and nums[i + 1] == 2:
            return True
    return False
  
def centered_average(nums):
  total_sum = sum(nums)
  Max = max(nums)
  Min = min(nums)
  avg = (total_sum - (Max + Min)) // (len(nums) - 2)
  return avg