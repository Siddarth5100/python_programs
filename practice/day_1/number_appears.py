'''
Return True if any number appears more than 2 times
'''
nums = [1,2,2,3,3,3]

def num_count():
    num_count = {}

    for num in nums:
        if not num in num_count:
            num_count[num] = 0
            for no in nums:
                if num == no:
                    num_count[num] += 1

    val = 0
    key_val = 0
    for key, value in num_count.items():
        if value > 2:
            val = value
            key_val = key
            return True
        
print(num_count())