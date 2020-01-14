#-------------------------------------------------------------------------------
# Some defined functions that would be used on an array of numbers, showing 
# different Data Structures.
#-------------------------------------------------------------------------------

def first_last6(nums):
  if nums[0] == 6 or nums[len(nums) - 1] == 6:   # function checks if the first
    return True                                  # or last number is 6. 
  else:
    return False

def same_first_last(nums):
  if len(nums) >= 1 and nums[0] == nums[len(nums) -1]: # checks if the first &
    return True                                        # last numbers are the 
  else:                                                # same.
    return False

def make_pi():                               # function creates an Array.
    make_pi=[3, 1, 4]
    return make_pi
  
def common_end(a, b):
  if a[0] == b[0] or a[len(a) -1] == b[len(b) -1]: # function checks if the two 
    return True                                    # variables entered have a 
  else:                                            # common end.
    return False

def sum3(nums):
  return nums[0] + nums[1] + nums[2]      # returns the sum of the first 3 ints.

def rotate_left3(nums):
  return [nums[1], nums[2], nums[0]]      # returns an array where the elments 
                                          # are shifted to the left.
                                          
def reverse3(nums):
  return [nums[2], nums[1], nums[0]]      # returns an array where the elments 
                                          # are reversed.

def max_end3(nums):
  if nums[0] > nums[2]:
    return [nums[0], nums[0], nums[0]]    # returns an array of the last int if 
  else:                                   # the last in is greater than the 
    return [nums[2], nums[2], nums[2]]    # first element & vice versa.
  
def sum2(nums):
  if len(nums) >= 2:                      # returns the sum of the first 2 ints.
    return nums[0] +nums[1]
  elif len(nums) == 1:
    return nums[0]
  else:
    return 0
  
def middle_way(a, b):
  return [a[1], b[1]]                     # returns an array consisting of the 
                                          # 2nd elements of the entered arrays.

def make_ends(nums):
  return [nums[0], nums[len(nums) -1]]    # returns an array consisting of the 
                                          # first & last elements of the entered 
                                          # array.
                                          

def count_evens(nums):
  count = 0                               # counts number of even ints in array.
  for num in nums:
    if num % 2 == 0:
      count = count + 1
  return count

def big_diff(nums):
  max = nums[0]
  min = nums[0]                           # returns the difference between the 
  for num in nums:                        # greatest 2 ints in an array.
    if num >= max:
      max = num 
    elif num <= min:     
      min = num
  return max - min

def has22(nums):
    for i in range(len(nums)-1):               # returns true if the array 
        if nums[i] == 2 and nums[i + 1] == 2:  # contains 2 consecutive elments 
            return True                        # with the value 2.
    return False
  
def centered_average(nums):                    # returns the centered_average 
  total_sum = sum(nums)                        # of the array.
  Max = max(nums)
  Min = min(nums)
  avg = (total_sum - (Max + Min)) // (len(nums) - 2)
  return avg