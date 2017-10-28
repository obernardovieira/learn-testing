import unittest
from todo import ToDo
from item import Item


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.todo = ToDo()

    def test_add(self):
        self.todo.add(Item("Ola"))
        self.assertEqual(1, self.todo.count())
        self.todo.add(Item("Xau"))
        self.assertEqual(2, self.todo.count())

    def test_remove(self):
        self.todo.add(Item("Ola"))
        self.todo.add(Item("Xau"))
        self.todo.remove("Ola")
        self.assertEqual(1, self.todo.count())


if __name__ == '__main__':
    unittest.main()
