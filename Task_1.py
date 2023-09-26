"""

Minion Work Assignments
=======================
Commander Lambda's minions are upset! They're given the worst jobs on the whole space station, and some of them are starting to complain that even those worst jobs are being allocated unfairly. If you can fix this problem, it'll prove your chops to Commander Lambda so you can get promoted!

Minions' tasks are assigned by putting their ID numbers into a list, one time for each day they'll work that task. As shifts are planned well in advance, the lists for each task will contain up to 99 integers. When a minion is scheduled for the same task too many times, they'll complain about it until they're taken off the task completely. Some tasks are worse than others, so the number of scheduled assignments before a minion will refuse to do a task varies depending on the task. You figure you can speed things up by automating the removal of the minions who have been assigned a task too many times before they even get a chance to start complaining.

Write a function called solution(data, n) that takes in a list of less than 100 integers and a number n, and returns that same list but with all of the numbers that occur more than n times removed entirely. The returned list should retain the same ordering as the original list - you don't want to mix up those carefully-planned shift rotations! For instance, if data was [5, 10, 15, 10, 7] and n was 1, solution(data, n) would return the list [5, 15, 7] because 10 occurs twice, and thus was removed from the list entirely.

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution([1, 2, 3], 0)
Output:


Input:
solution.solution([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)
Output:
    1,4

-- Java cases --
Input:
Solution.solution({1, 2, 2, 3, 3, 3, 4, 5, 5}, 1)
Output:
    1,4

Input:
Solution.solution({1, 2, 3}, 0)
Output:


Use verify [file] to test your solution and see how it does. When you are finished editing your code, use submit [file] to submit your answer. If your solution passes the test cases, it will be removed from your home folder.


"""

import numpy as np

data = [1, 2, 2, 3, 3, 3, 4, 5, 5]
n = 1
data1 = [1, 2, 3]
n1 = 0
data2  = [1, 2, 2, 3, 3, 3, 4, 5, 5, 6, 7, 7, 8, 8, 8, 9, 9]
n2 = 2
data3 = list(np.random.randint(1, 100, 98))
data4 = [15, 4, 5, 13, 3, 2, 6, 5, 17, 17, 2, 15, 13, 3, 19, 19, 1, 18, 6, 11, 4, 13, 5, 17, 13, 10, 9, 10, 9, 1, 4, 7, 6, 12, 17, 6, 18, 9, 11, 4, 8, 3, 10, 6, 2, 9, 11, 9, 16, 12, 1, 12, 15, 5, 1, 19, 11, 14, 17, 4, 5, 16, 12, 6, 11, 2, 15, 17, 9, 3, 16, 1, 13, 15, 18, 10, 19, 17, 15, 15, 14, 16, 6, 15, 4, 7, 15, 2, 4, 15, 19, 15, 16, 6, 16, 13, 17, 12]

def solution(data: list, n: int)-> list:
    a = []
    for number in data:
        count_number = data.count(number)
        if n == 0:
            data.clear()
        elif count_number > n:
            a.append(number)
    for num in a:
        data.remove(num)
    return data


a = solution(data, n)
c = solution(data1, n1)
d = solution(data2, n)
e = solution(data4, n)
b = solution(data3, n2)
print(a)
print(c)
print(d)
print(e)
print(len(b), b)

