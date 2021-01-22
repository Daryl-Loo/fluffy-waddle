"""
Task:
Write a function that sorts a list of numbers in ascending order.
Logic:
This task is a simple sorting task. While there are many ways, such as using built in methods or sorting algorithm to solve this, we will not be using any of these methods.
If you wish to learn about  algorithms, you should do FIT1045/FIT1008/FIT2004, where you will learn sorting algorithms that is much more efficient than the method I am showing you.
Instead what we will be doing, is simply selecting the minimum element of the list, and putting it in another.
The idea is you will have 2 list, the first list is the input, and you will take the current smallest element, and put it in the second list.
The second list grows, and is always sorted in ascending order, while the first list shrinks
Returning the second list after the first list is empty means you will have the original list sorted in ascending order
"""


def sortLstAsc(lst):
    """
    This function sorts the list in ascending order. It calls on the function findMinIndex() to find the min index.
    You could just take the code from the function and substitute it in, but it would be less readable.
    :param lst: a list of numbers.
    :return: a list of numbers, sorted in ascending order
    """
    reVal = []  # An empty list. We are adding numbers to it, and we are returning this list at the end
    while len(lst) != 0:  # while the list is not empty.
        minIndex = findMinIndex(
            lst)  # We find the minimum index of the current lst, and assign it to the variable minIndex
        minNum = lst.pop(
            minIndex)  # We remove the minimum element from lst, and assign the number to the variable minNum
        reVal.append(minNum)  # We append(add) the number in minNum to the list reVal
    return reVal


def findMinIndex(lst):
    """
    This function returns the index where the minimum index is at
    It goes through each element, and if it finds an element smaller than the its current minIndex, it changes its value to that index
    :param lst: a list of numbers.
    :return: an integer, which represents the index where the minimum is at
    """
    reVal = 0  # we default it to 0, which is the first element of a list.
    for i in range(len(lst)):  # for every element in this lst
        if lst[reVal] > lst[i]:  # if the element is smaller than the number at index reVal
            reVal = i  # change reVal to the index of the element
    return reVal


def test():
    """
    This function is just to check if the test works.
    Uses builtin python methods to sort the list, and uses that list to verify the output of the function sortLstAsc()
    When testing your code, try to think of cases where it might fail, and test it to ensure it does not. When testing, your goal is to break your code, so you can fix it up.
    For sorting algorithms, think what if the list is empty? Already sorted? Has duplicates? Has negative values?
    :return:
    """
    lst1 = [1, 2, 3, 4, 5]
    lst2 = [5, 4, 3, 2, 1]
    lst3 = [1, 2, 3, 3, 2, 1]
    lst4 = [-8, -1, 4, -1, -9]

    lst5 = sorted(lst1)
    lst6 = sorted(lst2)
    lst7 = sorted(lst3)
    lst8 = sorted(lst4)

    lst9 = []
    assert sortLstAsc(lst1) == lst5, "Test failed, does not work with list already sorted in ascending "
    assert sortLstAsc(lst2) == lst6, "Test failed, does not work with list sorted in descending order"
    assert sortLstAsc(lst3) == lst7, "Test failed. Does not handle with list with duplicate values"
    assert sortLstAsc(lst4) == lst8, "Test failed. Does not handle list with negative integers"
    assert sortLstAsc(lst9) == lst9, "Test failed. Does not handle empty list"
    return True


print(test())
