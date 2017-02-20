"""Intro to Python - Week 1 - Quiz."""


# Question 1
def question_1():
    """Return the correct answer for the following question.

    What's the correct data type of the following values: `True`, `False`

    a) Integer
    b) Boolean
    c) String
    d) Collection
    """
    # Return the correct value.
    return 'Boolean'


# Question 2
def question_2():
    """Return the correct answer for the following question.

    What's the final result of the following operation:

    user = True or ("" and False and []) or (1 and "hello world")

    a) []
    b) 1
    c) True
    d) "hello world"
    """
    # Return the correct value.
    return True


# Question 3
def remove_Es(a_string):
    """Implement the code required to make this function work.

    Write a function `remove_Es` that receives a string and removes all
    the characters `'e'` or `'E'`. Example:

    remove_Es('remoter')  # 'rmotr'
    remove_Es('eEe')      # ''
    remove_Es('abc')      # 'abc'
    """
    # Write your code here
    # return a_string.replace('e', '').replace('E', '')  (alternative)
    result = ""
    for char in a_string:
        # if char not in ('e', 'E'):  (alternative)
        if char != 'e' and char != 'E':
            result += char
    return result


# Question 4
def question_4():
    """Return the correct answer for the following question.

    Given the following two collections:

    a_tuple = (19, 33, 12)
    a_list = range(0, 10)

    What's the final value of `result`?

    result = a_list[3**2 - 8] + a_list[-1] + a_tuple[2]
    """
    # Return the correct value.
    return 22


# Question 5
def swap_keys_and_values(a_dict):
    """Implement the code required to make this function work.

    Write a function `swap_keys_and_values` that receives a dictionary
    and returns a new dictionary with the keys and values swapped.
    **Important!** Do not modify the original one.

    Example:

    prices = {
      'apples': 1.89,
      'oranges': 1.17,
      'peaches': 2.21
    }

    swapped = swap_keys_and_values(prices)
    print(swapped)
    {
      1.89: 'apples',
      1.17: 'oranges',
      2.21: 'peaches'
    }
    """
    # Write your code here
    swapped = {}
    for k, v in a_dict.items():
        swapped[v] = k
    return swapped


# Question 6
def matrix_sum(a_matrix):
    """Implement the code required to make this function work.

    Write a function `matrix_sum` that sums all the values in a square matrix.
    Example:

    m1 = [
        [2, 9, 1],
        [3, 1, 18],
        [22, 8, 16]
    ]
    m2 = [
      [81, 29],
      [31, 57]
    ]

    matrix_sum(m1)  #  80
    matrix_sum(m2)  # 198
    """
    # Write your code here
    result = 0
    for row in a_matrix:
        for c in row:
            result += c
    return result
