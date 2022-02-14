from linked_list import MyLinkedList
import unittest


class TestLinkedList(unittest.TestCase) :

    # def test_get(self) :
    #     new = MyLinkedList()
    #     new.addAtHead(1)
    #     self.assertEqual(new.head.val, 1)
    #     new.addAtTail(3)
    #     self.assertEqual(new.get(1), 3)
    #     new.addAtHead(2)
    #     self.assertEqual(new.get(0), 2)
    #     self.assertEqual(new.get(1), 1)
    #     new.addAtIndex(2, 4)
    #     self.assertEqual(new.get(3), 3)
    #     self.assertEqual(new.get(2), 4)

    # def test_addAtHead(self) :
    #     new = MyLinkedList()
    #     new.addAtHead(18)
    #     self.assertEqual(new.head.val, 18)
    #     new.addAtHead(17)
    #     self.assertEqual(new.head.val, 17)
    #     new.addAtHead(16)
    #     self.assertEqual(new.head.val, 16)

    # def test_addAtTail(self) :
    #     new = MyLinkedList()
    #     new.addAtTail(18)
    #     new.addAtTail(17)
    #     new.addAtTail(16)
    #     self.assertEqual(new.head.val, 18)
    #     self.assertEqual(new.head.next.val, 17)
    #     self.assertEqual(new.head.next.next.val, 16)

    # def test_addAtIndex(self) :
    #     new = MyLinkedList()
    #     new.addAtHead(1)
    #     new.addAtHead(2)
    #     new.addAtHead(3)
    #     new.addAtHead(4)
    #     self.assertEqual(new.head.val, 4)
    #     new.addAtIndex(0, 5)
    #     self.assertEqual(new.head.val, 5)
    #     new.addAtIndex(0, 18)
    #     self.assertEqual(new.head.val, 18)
    #     new.addAtIndex(3, 16)
    #     self.assertEqual(new.get(3), 16)
    #     self.assertEqual(new.get(4), 3)
    #     self.assertEqual(new.get(5), 2)

    def test_deleteAtIndex(self) :
        new = MyLinkedList()
        new.addAtIndex(0, 1)
        new.addAtIndex(1, 2)
        new.addAtIndex(2, 3)
        new.addAtIndex(3, 4)
        new.addAtIndex(4, 5)
        new.deleteAtIndex(2)
        self.assertEqual(new.get(0), 1)
        self.assertEqual(new.get(1), 2)
        self.assertEqual(new.get(2), 4)
        self.assertEqual(new.get(3), 5)
        new.deleteAtIndex(0)
        self.assertEqual(new.get(0), 2)
        new.deleteAtIndex(2)
        self.assertEqual(new.get(1), 4)
        new.deleteAtIndex(2)
        self.assertEqual(new.get(1), 4)

if __name__ == '__main__':
    unittest.main()
