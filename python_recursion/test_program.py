import unittest
import program


class TestProgram(unittest.TestCase):
    # def test_case_1(self):
    #     self.assertEqual(program.identical([1,2,3],[1,2]), False)

    def test_case_2(self):
        self.assertEqual(program.identical([1,2,3],[1,2,3]), True)
if __name__ == "__main__":
    unittest.main()
