def duplicate(nums):
    masiv = []
    for num in nums:
        if num in masiv:
            return True
        masiv.append(num)

    return False

numbers = [1, 1, 4, 4, 6]


print(duplicate(numbers))