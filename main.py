"""Intro to Python - Week 1 - Quiz."""


# Question 1
def question_1():
    """Return the correct answer for the following question.

    What's the correct data type of the following values: True, False

    a) Integer
    b) Boolean
    c) String
    d) Collection
    """
    return 'Boolean'


# Question 2
def question_2():
    """Return the correct answer for the following question.

    What's the final result of the following operation:

    result = True or ("" and False and []) or (1 and "hello world")

    a) []
    b) 1
    c) True
    d) False
    e) "hello world"
    """
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
    b_string = ''
    for i in a_string:
        if i != 'e' and i != 'E':
            b_string += i
    return b_string
    


# Question 4
def question_4():
    """Return the correct answer for the following question.

    Given the following two collections:

    a_tuple = (19, 33, 12)
    a_list = range(0, 10)

    What's the final value of `result`?

    result = a_list[3**2 - 8] + a_list[-1] + a_tuple[2]
    """
    return 22


# Question 5
def calculate_tax(income):
    """Implement the code required to make this function work.

    Write a function `calculate_tax` that receives a number (`income`) and
    calculates how much of Federal taxes is due,
    according to the following table:


    | Income  | Tax Percentage |
    | ------------- | ------------- |
    | <= $50,000    |        15%    |
    | <= $75,000    |        25%    |
    | <= $100,000   |        30%    |
    | > $100,000    |        35%    |

    Example:

    income = 30000  # $30,000 is less than $50,000
    calculate_tax(income)  # $30,000 * 0.15  = 4500 = $4,500

    income = 80000  # $80,000 is more than $75,000 but less than $80,000
    calculate_tax(income)  # $80,000 * 0.25 = 20000 = $20,000

    income = 210000  # $210,000 is more than $100,000
    calculate_tax(income)  # $210,000 * 0.35 = 73500 = $73,500
    """
    tax = 0
    if income <= 50000:
        tax += (income *.15)
        return tax
    elif income >= 50000 and income <= 75000:
        tax += (income * .25)
        return tax
    elif income >= 75000 and income <= 100000:
        tax += (income * .30)
        return tax
    elif income >= 100000:
        tax += (income * .35)
        return tax


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
    result = 0
    for row in a_matrix:
        for col in row:
            result += col
        return result
