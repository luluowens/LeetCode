'''Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
'''

class MinStack:

    def __init__(self):
        self.values = []
        self.min = None

    def push(self, val: int) -> None:
        self.values = [val] + self.values
        if not self.min :
            self.min = val
        elif self.min >= val :
            self.min = val

    def pop(self) -> None:
        first = self.values[0]
        self.values = self.values[1:]
        if first == self.min :
            self.min = min(self.values)

    def top(self) -> int:
        return self.values[0]

    def getMin(self) -> int:
        return self.min
        

import unittest

class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        my_sol = MinStack()
        my_sol.push(-2)
        my_sol.push(0)
        my_sol.push(-3)
        self.assertEqual(my_sol.getMin(), -3)
        my_sol.pop()
        self.assertEqual(my_sol.top(), 0)
        self.assertEqual(my_sol.getMin(), -2)
        

if __name__ == '__main__':
    unittest.main()

# minStack = MinStack()
# minStack.push(-2)
# minStack.push(0)
# minStack.push(-3)
# minStack.getMin()   # return -3
# minStack.pop()
# minStack.top()      # return 0
# minStack.getMin()   # return -2