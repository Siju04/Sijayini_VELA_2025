# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

def contains_duplicate(nums):
    # Use a set to keep track of unique elements
    unique_elements = set()

    for num in nums:
        # If the element is already in the set, it's a duplicate
        if num in unique_elements:
            return True
        else:
            # Add the element to the set
            unique_elements.add(num)

    # If the loop completes without finding duplicates, return False
    return False

# Example usage:
numbers = [1, 2, 3, 4, 5]
result = contains_duplicate(numbers)
print("Contains Duplicate:", result)
