from FibonacciNumbers.fibonacci_numbers import Solution
import unittest


class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        my_sol = Solution()
        self.assertEqual(my_sol.fib(2), 1)
        self.assertEqual(my_sol.fib(3), 2)
        self.assertEqual(my_sol.fib(4), 3)
        self.assertEqual(my_sol.fib(6), 8)

if __name__ == '__main__':
    unittest.main()
