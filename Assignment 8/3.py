# Write a Python class to get all possible unique subsets from a set of distinct integers Input : [4, 5, 6] Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]] 

class SubsetGenerator:
    def generate_subsets(self, nums):
        def backtrack(start, subset):
            if start == len(nums):
                result.append(subset[:])
                return
            subset.append(nums[start])
            backtrack(start + 1, subset)
            subset.pop()
            backtrack(start + 1, subset)

        result = []
        backtrack(0, [])
        return result

# Usage
generator = SubsetGenerator()
print(generator.generate_subsets([4, 5, 6]))
