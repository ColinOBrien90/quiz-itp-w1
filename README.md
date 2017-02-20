# Intro to Python - Week 1 - Quiz

This small quiz is just for validating the concepts covered during the first week of our course. It's **not something you can pass or fail**. We use the results of this quiz to evaluate if we need to add more support sessions or improve any aspect of the course.

**PLEASE, don't cheat**. Make it honest. We'll never share the data with the rest of the class.

_To complete this quiz, fork the repo, work on main.py and submit a Pull Request_

#### Question 1

What's the correct data type of the following values: `True`, `False`

##### Options:

```
a) Integer
b) Boolean
c) String
d) Collection
```

#### Question 2

What's the final result of the following operation:

```python
result = True or ("" and False and []) or (1 and "hello world")
```

##### Options:
```
a) []
b) 1
c) True
d) False
e) "hello world"
```

#### Question 3

Write a function `remove_Es` that receives a string and removes all the characters `'e'` or `'E'`. Example:

```python
remove_Es('remoter')  # 'rmotr'
remove_Es('eEe')      # ''
remove_Es('abc')      # 'abc'
```

#### Question 4

Given the following two collections:

```python
a_tuple = (19, 33, 12)
a_list = range(0, 10)
```

What's the final value of `result`?

```python
result = a_list[3**2 - 8] + a_list[-1] + a_tuple[2]
```

#### Question 5

Write a function `calculate_tax` that receives a number (`income`) and calculates
how much of Federal taxes is due, according to the following table:


| Income  | Tax Percentage      |
| ------------- | ------------- |
| <= $50,000    |        15%    |
| <= $75,000    |        25%    |
| <= $100,000   |        30%    |
| > $100,000    |        35%    |

Example:

```python
income = 30000  # $30,000 is less than $50,000
calculate_tax(income)  # $30,000 * 0.15  = 4500 = $4,500

income = 80000  # $80,000 is more than $75,000 but less than $80,000
calculate_tax(income)  # $80,000 * 0.25 = 20000 = $20,000

income = 210000  # $210,000 is more than $100,000
calculate_tax(income)  # $210,000 * 0.35 = 73500 = $73,500
```

#### Question 6

Write a function `matrix_sum` that sums all the values in a square matrix.

Example:

```python
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
```
