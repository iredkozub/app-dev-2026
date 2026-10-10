### Мое решение
## Решение в лоб
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range(n):
            for j in range (i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
# Два вложенных цикла - О(n^2); 1720 ms, 19,85 MB

##  Через dict
class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
       hm = {}
       for i, num in enumerate(nums):
            hm[num] = i
       for i, num in enumerate(nums):
            k = target - num
            if k in hm and hm[k] != i:
                return[i, hm[k]] 
# O(n), 0 ms, 20,58 MB

## Вывод: через hash map код выполняется быстрее, ниже вычислительная сложность, но похоже используется чуть больше памяти



### Решение агента 
##1
def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# Time complexity: O(n) - single pass through the array
# Space complexity: O(n) - hash map stores at most n elements

# The approach stores each number's index as we iterate. 
# For each number, we check if its complement (target - num) was already seen. 
# If so, we found the pair.

##2
def twoSum2(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

# Time complexity: O(n²) - nested loops check all pairs
# Space complexity: O(1) - only uses constant extra space

### Сравнение 

# Агент предложил два корректных решения и правильно определил их сложность: 
# O(n²) по времени и O(1) по памяти для двух вложенных циклов, 
# O(n) по времени и O(n) по памяти для HashMap.
# Моё решение через dict использует два последовательных прохода по списку, 
# а агент предложил вариант с одним проходом. Оба имеют временную сложность O(n), 
# но вариант агента может выполнять меньше операций. 
# Ошибок в алгоритмах агента нет