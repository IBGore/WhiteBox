import unittest
import fibonacci as f


# def test_fib():
#     assert(f.fib(1) == 0)

class TestCase(unittest.TestCase):
    #Base Cases
    def test_fib(self):
        self.assertEqual(f.fib(1),0)

    def test_fib1(self):
        self.assertEqual(f.fib(2),1)

    #recursive cases
    def test_fib2(self):
        self.assertEqual(f.fib(3),1)

    def test_fib3(self):
        self.assertEqual(f.fib(4),2)

    def test_fib4(self):
        with self.assertRaises(AssertionError):
            f.fib(-1)


    #Factorial Tests
    #Base Case
    def test_fact(self):
        self.assertEqual(f.fact(0),1)

    #Other cases
    def test_fact(self):
        self.assertEqual(f.fact(1),1)

    def test_fact(self):
        self.assertEqual(f.fact(2),2)

    def test_fact(self):
        self.assertEqual(f.fact(3),6)

    def test_fib4(self):
        with self.assertRaises(AssertionError):
            f.fact(-1)


        

    


if __name__ == '__main__':
    unittest.main(verbosity=2)

