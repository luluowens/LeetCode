'''Design a data structure that accepts a stream of integers and checks if it
has a pair of integers that sum up to a particular value.

Implement the TwoSum class:

TwoSum() Initializes the TwoSum object, with an empty array initially.
void add(int number) Adds number to the data structure.
boolean find(int value) Returns true if there exists any pair of numbers
whose sum is equal to value, otherwise, it returns false.
'''

class TwoSum:

    def __init__(self):
        self.values = []
        self.sums = set()

    def add(self, number: int) -> None:
        for i in range(len(self.values)) :
            self.sums.add(self.values[i] + number)
        self.values.append(number)

    def find(self, value: int) -> bool:
        return value in self.sums


import unittest

class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        my_sol = TwoSum()
        my_sol.add(3)
        my_sol.add(2)
        my_sol.add(1)
        self.assertEqual(my_sol.find(2), False)
        # my_sol.pop()
        # self.assertEqual(my_sol.top(), 0)
        # self.assertEqual(my_sol.getMin(), -2)
        

if __name__ == '__main__':
    unittest.main()


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)