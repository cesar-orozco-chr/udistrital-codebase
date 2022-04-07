import unittest
from main import junquillo_chino

VALUES =[
    (3, 30, 3.6),
    (10, 20, 62.4),
    (5, 25, 12.4),
    (0, 0, 0)
]

class TestJunquilloChino(unittest.TestCase):
    def __init__(self, d, h, output) -> None:
        super(TestJunquilloChino,self).__init__()
        self.d = d
        self.h  = h
        self.output = output

    def runTest(self):
        self.assertEqual(junquillo_chino(self.d, self.h), self.output)

def suite():
    suite = unittest.TestSuite()
    suite.addTests([ TestJunquilloChino(d,h,output) for d, h, output in VALUES])
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())