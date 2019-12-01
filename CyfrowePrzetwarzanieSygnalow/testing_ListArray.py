from strategia_redukcji import ListArray
import unittest


class TestinglistArray(unittest.TestCase):
    def setUp(self):
        self.a = \
            [['a', 'b', 'c', 'g'],
             ['d', 'e', 'f', 'x'],
             ['q', 't', 'i', 'y'],
             ['i', 'o', 'p', 's']]

        self.b = \
            [['a', 'c', 'j', 'v'],
             ['d', 'e', 'f', 'x'],
             ['q', 't', 'i', 'y'],
             ['i', 'o', 'p', 's']]

    def test_equal(self):

        A = ListArray(self.a)
        B = ListArray(self.b)
        Aprim = ListArray(self.a)
        cut_A = A[2:,0:2]
        cut_B = B[2:,0:2]

        assert A == Aprim
        assert not A == B        
        assert cut_A == cut_B
        assert A[2] == ListArray([['q', 't', 'i', 'y']])
        assert A[2] == ListArray(['q', 't', 'i', 'y'])

    def test_row_len(self):
        A = ListArray(self.a)
        

    def test_traspose(self):
        A = ListArray(self.a)
        A2 = A.transp()

if __name__ == '__main__':
    unittest.main()
