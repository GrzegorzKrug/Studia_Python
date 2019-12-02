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
        cut_A = A[2:, 0:2]
        cut_B = B[2:, 0:2]

        assert A == Aprim
        assert not A == B
        assert cut_A == cut_B

        # print("A2 \n\t", A[2])
        # print("List \n\t", ListArray(['q', 't', 'i', 'y']))
        assert A[2] == ListArray([['q', 't', 'i', 'y']])
        assert A[2] == ListArray(['q', 't', 'i', 'y'])

    def test_fit(self):
        a = \
            [['a', 'b', 'a', 'b'],
             ['a', 'b', 'a', 'b']]

        b = [['a', 'b'],
             ['c', 'd']]
        c = ['a', 'b', 'c']

        A = ListArray(a)
        B = ListArray(b)
        C = ListArray(c)

        assert A.fit()
        assert not B.fit()
        self.assertRaises(ValueError, C.fit)

    def test_traspose(self):
        a = [['a', 'g'],
             ['b', 'x']]
        b = [['a', 'b'],
             ['g', 'x']]

        a2 = [['a', 'g', 'j'],
              ['b', 'x', 'k']]

        b2 = [['a', 'b'],
              ['g', 'x'],
              ['j', 'k']]

        A = ListArray(a)
        B = ListArray(b)

        A2 = ListArray(a2)
        B2 = ListArray(b2)
        assert A.transp() == B
        assert A2.transp() == B2

    def test_mult(self):
        a = [['a', 'g'],
             ['b', 'x']]

        b = [['b', 'b'],
             ['d', 'b']]
        res1 = [['a*a + b*g', 'a*g + x*g'],
                ['b*a + x*b', 'g*b + x*x']]
        res2 = [['a*b + d*g', 'a*b + b*g'],
                ['b*b + d*x', 'b*b + x*b']]

        A = ListArray(a)
        B = ListArray(b)
        Res1 = ListArray(res1)
        Res2 = ListArray(res2)

        assert(A*A == Res1)
        assert(A*B == Res2)

    # def test_row_len(self):
    #     A = ListArray(self.a)
    #     for a in A:
    #         # pass
    #         print('a', a == ListArray(['d','e','f','x']))


if __name__ == '__main__':
    unittest.main()
