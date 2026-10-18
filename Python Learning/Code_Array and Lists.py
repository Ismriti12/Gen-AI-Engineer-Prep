#Find the second-largest element in an array.

# arr1 = [1, 2, 3, 4, 5, 2] #second largest element is 4

# arr2 = [-1, -5, 0, 100, 4] #second largest element is 4

# arr3 = [567, 74, 999, 88, 54] #second largest element is 567

# arr4 = [-8,-10, -6, -5, -4, -8] #second largest element is -5

# arr5 = [1, 2, 3, 4, 1, 3] #second largest element is 3

# Edge cases
# 1. null array or array length <2
# 2. duplicates in the array

# Approach: we can also use set and sort
# find which is the most efficient approach
# Approach 1

def second_largest_element_in_array1(input_list:list[int]) -> int:
    if len(input_list) < 2:
        return None
    #sort returns None
    input_list.sort()
    return input_list[len(input_list)-2]

#Approach 2

def second_largest_element_in_array2(input_list:list[int]) -> int:
    if len(input_list) < 2:
            return None
     # Initialize both tracking variables to negative infinity
    largest = float('-inf')
    second_largest = float('-inf')
    for num in range(len(input_list)):
        if input_list[num] > largest:
             second_largest = largest
             largest = input_list[num]
    return second_largest


# print("second_largest_element_in_array1")
# print(second_largest_element_in_array1(arr1))
# print(second_largest_element_in_array1(arr2))
# print(second_largest_element_in_array1(arr3))
# print(second_largest_element_in_array1(arr4))
# print(second_largest_element_in_array1(arr5))

# print("second_largest_element_in_array2")
# print(second_largest_element_in_array2(arr1))
# print(second_largest_element_in_array2(arr2))
# print(second_largest_element_in_array2(arr3))
# print(second_largest_element_in_array2(arr4))
# print(second_largest_element_in_array2(arr5))

# Find the missing number in an array containing numbers from 1 to N.

# arr1 = [1,3,4,5]

# Approach 1: arithmetic -- can only find one missing number
# Approach 2: XOR -- #arr2 = [1, 3, 5, 6, 7]
# Approach 3: line by line -- can find missing by index, can be implemented using hashmap

def find_missing_number1(input_list: list[int]) -> int:
       # last number will never be missing?
       n = input_list[len(input_list)-1]       
       expected_sum = n * (n+1)//2
       print(expected_sum)
       original_sum = sum(input_list)
       print(original_sum)
       return expected_sum - original_sum

# print("find_missing_number1")
# print(find_missing_number1(arr1))


# Remove duplicates from a list while preserving order

# inp_list = [1,2,2,3,4, 6, 7, 8, 5]

# cannot use set as set is unordered
# we can use dictionary
def remove_duplicates(input_list: list[int]) -> list[int]:
     seen = []
     # why to make seen as set
     duplicates = []

     for num in input_list:
          if num in seen:
               duplicates.append(num)
          else:
               seen.append(num)
               #how to append in a set

     return list(seen)

# print("remove_duplicates")
# print(remove_duplicates(inp_list))

# Move all zeros to the end without changing the order of other elements.

#input = [0, 5, 4, 3, -1, 0, -2]
#output = [5,4,3,-1,-2,0,0]

def move_zeroes_to_end(input_list: list[int]) -> list[int]:
     # shift all the numbers by 1 iteration mehnat
     # how to remove list element from between so that no other element is affected

    #two pointer approach
    p1 = 0
    p2 = 0 
    count = []
    for i, num in enumerate(input_list):

        if num == 0 :
            p1 = i
            p2 = i+1   
            count.append(0)                         
            input_list[p1] = input_list[p2]


# Merge two sorted arrays into one sorted array.

list1 = [1,2,3,4,5,6]
list2 = [0,1,2]

def merge_two_sorted_arrays(list1:list[int], list2: list[int]) -> list[int]:
     ans = []
     i = 0
     cmp = 0 
     if len(list1)<len(list2):
          cmp = len(list1)
     else :
          cmp = len(list2)
     while i<cmp:
         if  list1[i]<list2[i]:
              ans.append(list1[i])
              print("if",ans)
         elif list1[i]==list2[i]:
              ans.append(list1[i])
              ans.append(list2[i])
              print("elif", ans)      
         else:
              ans.append(list2[i])
              print("else",ans)
         i+=1

     if i==len(list1) and i<len(list2):
          ans.extend(list2)
     else:
          ans.extend(list1)
     return ans
print("merge_two_sorted_arrays")        
print(merge_two_sorted_arrays(list1,list2))

#Find two numbers that add up to a target.	Hash map, Two Sum
#can we give the size of list in the function declaration
#Approach: we can use hashmap to store the numbers and their indices, then check if the complement (target - current number) exists in the hashmap. 
def two_sum(inp_list: list[int], target: int)-> list[int]:
     seen={}
     ans = []
     for i, num in enumerate(inp_list):
          if target-num in seen:
               #can we append using comma
               ans.append(seen[target-num])
               ans.append(i)
               return ans
          else:
            seen[num] = i 
     # EDGE CASE: If the loop finishes, no pair exists
     return [] 
     

print("two sum \n ", two_sum([2,7,3,6,5],9))

#Approach: we can use two pointers, one starting from the beginning and the other from the end of the array. 
# We can move the pointers based on the sum of the elements at those pointers compared to the target.
def two_sum_two_pointers(inp_list: list[int], target: int)-> list[int]:
     sorted_pairs = sorted([(num,i)for i, num in enumerate(inp_list)])
     print("sorted_pairs", sorted_pairs)
     left = 0
     right = len(inp_list)-1
     while left<right:
          if sorted_pairs[left][0]+sorted_pairs[right][0] == target:
               return [sorted_pairs[left][1], sorted_pairs[right][1]]
          elif sorted_pairs[left][0] + sorted_pairs[right][0] < target:
               left+=1
          else:
               right-=1
     return[]


print("two sum two pointers\n ", two_sum_two_pointers([2,7,3,6,5],9))


# 6	Find the intersection of two arrays.	Sets, hashing

l1= [1, 2, 3, 4, 5]
l2 = [3, 4, 5, 6, 7]
#intersection = [3, 4, 5]

def intersection_of_two_arrays1(list1: list[int], list2: list[int]) -> list[int]:
     set1 = set(list1)
     set2 = set(list2)
     return list(set1.intersection(set2))

def intersection_of_two_arrays2(list1: list[int], list2: list[int]) -> list[int]:
     result = set()
     for num in list2:
          if num in list1:
               result.add(num)
     return list(result)

print("intersection of two arrays1", intersection_of_two_arrays1(l1, l2))
print("intersection of two arrays2", intersection_of_two_arrays2(l1, l2))


# 7	Merge two sorted arrays into one sorted array.	Two pointers

# Example 1: Standard Case (Different Sizes)

# • Input Array 1: [1, 3, 5]
# • Input Array 2: [2, 4, 6, 8]
# • Output Array: [1, 2, 3, 4, 5, 6, 8]

# Example 2: Arrays with Overlapping & Duplicate Values

# • Input Array 1: [1, 2, 4, 5]
# • Input Array 2: [2, 3, 5, 6]
# • Output Array: [1, 2, 2, 3, 4, 5, 5, 6] (Duplicates are preserved)

# Example 3: One Array is Entirely Larger

# • Input Array 1: [1, 2, 3]
# • Input Array 2: [10, 20]
# • Output Array: [1, 2, 3, 10, 20]

# Example 4: Edge Case (Empty Arrays)

# • Input Array 1: []
# • Input Array 2: [5, 6, 7]
# • Output Array: [5, 6, 7]

#using sets - Approach 1
def merge_sorted_arrays_set(list1: list[int], list2: list[int]) -> list[int]:
     #this won't preserve duplicates, but will give unique elements in sorted order
     return sorted(set(list1).union(set(list2)))

#using two pointers - Approach 2
def merge_sorted_arrays_two_pointers(list1: list[int], list2: list[int]) -> list[int]:
     merged_list = []
     i, j = 0, 0
     while i < len(list1) and j < len(list2):
          if list1[i] < list2[j]:
               merged_list.append(list1[i])
               i += 1
          else:
               merged_list.append(list2[j])
               j += 1
     # Append remaining elements
     while i < len(list1):
          merged_list.append(list1[i])
          i += 1
     while j < len(list2):
          merged_list.append(list2[j])
          j += 1
     return merged_list

#Approach 3: Using built-in sort function
def merge_sorted_arrays_builtin(list1: list[int], list2: list[int]) -> list[int]:
     return sorted(list1 + list2)


# 8	Find the maximum sum of a contiguous subarray.
def generate_sub_arrays(input_list: list[int]) -> list[list[int]]:
    subarrays = []
    for i in range(len(input_list)):
         for j in range(i+1, len(input_list)+1):
              subarrays.append(input_list[i:j])
    return subarrays

def max_sub_array(input_list:list[int]):
     subarrays = []
     subarrays = generate_sub_arrays(input_list)
     max_sum = float('-inf')
     for list in subarrays:
          subarray_sum = sum(list)
          max_sum = (subarray_sum, max_sum)

     return max_sum

def max_sub_array_kadane(input_list: list[int]) -> int:
     current_sum = 0
     max_sum = float('-inf')
     for num in input_list:
          current_sum+= num
          #writing this line before if current_sum<0 
          #incase all numbers are negative, we want to keep track of the maximum sum seen so far
          max_sum = max(current_sum, max_sum)

          if current_sum<0:
               current_sum = 0
     return max_sum


# Test Case 1: Standard mixed array



input_1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


# Test Case 2: All negative numbers
input_2 = [-5, -2, -3, -1, -4]


# Test Case 3: All positive numbers
input_3 = [1, 2, 3, 4, 5]


# Test Case 4: Single element array
input_4 = [7]

print("input1 =", input_1)
print("\n",generate_sub_arrays(input_1))
print(f"Input 1:  {input_1}")
print(f"Output 1: {max_sub_array(input_1)} (Expected: 6 -> from [4, -1, 2, 1])\n")
print(f"Output 1 using Kadane's Algorithm: {max_sub_array_kadane(input_1)} (Expected: 6 -> from [4, -1, 2, 1])\n")
print("input2 =", input_2)
print("\n",generate_sub_arrays(input_2))
print(f"Input 2:  {input_2}")
print(f"Output 2: {max_sub_array(input_2)} (Expected: -1 -> from [-1])\n")
print(f"Output 2 using Kadane's Algorithm: {max_sub_array_kadane(input_2)} (Expected: -1 -> from [-1])\n")
print("input3 =", input_3)
print("\n",generate_sub_arrays(input_3))
print(f"Input 3:  {input_3}")
print(f"Output 3: {max_sub_array(input_3)} (Expected: 15 -> from the whole array)\n")
print(f"Output 3 using Kadane's Algorithm: {max_sub_array_kadane(input_3)} (Expected: 15 -> from the whole array)\n")
print("input4 =", input_4)
print("\n",generate_sub_arrays(input_4))
print(f"Input 4:  {input_4}")
print(f"Output 4: {max_sub_array(input_4)} (Expected: 7)\n")
print(f"Output 4 using Kadane's Algorithm: {max_sub_array_kadane(input_4)} (Expected: 7)\n")