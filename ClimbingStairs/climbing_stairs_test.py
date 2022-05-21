from ClimbingStairs.climbing_stairs import Solution
import unittest


class TestLinkedList(unittest.TestCase) :

    def test_solution(self) :
        my_sol = Solution()
        self.assertEqual(my_sol.climbStairs(2), 2)
        self.assertEqual(my_sol.climbStairs(3), 3)
        self.assertEqual(my_sol.climbStairs(4), 5)
        self.assertEqual(my_sol.climbStairs(6), 13)

if __name__ == '__main__':
    unittest.main()
