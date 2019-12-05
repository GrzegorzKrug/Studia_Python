from reduction_strategy import SymArray
import unittest


class TestingSymArray(unittest.TestCase):
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
        A = SymArray(self.a)
        B = SymArray(self.b)
        Aprim = SymArray(self.a)
        cut_A = A[2:, 0:2]
        cut_B = B[2:, 0:2]

        self.assertEqual(A, Aprim)
        self.assertFalse(A == B)
        self.assertEqual(cut_A, cut_B)

        self.assertTrue(A[2] == SymArray([['q', 't', 'i', 'y']]))
        self.assertTrue(A[2] == SymArray(['q', 't', 'i', 'y']))

    def test_fit(self):
        a = \
            [['a', 'b', 'a', 'b'],
             ['a', 'b', 'a', 'b']]

        b = [['a', 'b'],
             ['c', 'd']]
        c = ['a', 'b', 'c']

        A = SymArray(a)
        B = SymArray(b)
        C = SymArray(c)

        self.assertTrue(A.match_patern_any())
        self.assertFalse(B.match_patern_any())
        self.assertRaises(ValueError, C.match_patern_any)

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

        A = SymArray(a)
        B = SymArray(b)
        A2 = SymArray(a2)
        B2 = SymArray(b2)

        self.assertEqual(A.transp(), B)
        self.assertEqual(A2.transp(), B2)

    def test_add(self):
        a = [['a', 'g'],
             ['b', 'x']]

        b = [['b', 'b'],
             ['d', 'b']]
        res1 = [['a+b', 'g+b'], ['b+d', 'b+x']]
        res2 = [['b+b', 'b+b'], ['d+d', 'b+b']]
        A = SymArray(a)
        B = SymArray(b)
        res1 = SymArray(res1)
        res2 = SymArray(res2)

        self.assertEqual(A + B, res1)
        self.assertEqual(B + B, res2)

    def test_sub(self):
        a = [['a', 'g'],
             ['b', 'x']]

        b = [['b', 'b'],
             ['d', 'b']]
        res1 = [['a-b', 'g-b'], ['b-d', 'x-b']]
        res2 = [['b-b', 'b-b'], ['d-d', 'b-b']]

        A = SymArray(a)
        B = SymArray(b)
        res1 = SymArray(res1)
        res2 = SymArray(res2)

        self.assertEqual(A - B, res1)
        self.assertEqual(B - B, res2)

    def test_mult(self):
        a = [['a', 'g'],
             ['b', 'x']]

        b = [['b', 'b'],
             ['d', 'b']]
        res1 = [['a*a + b*g', 'a*g + x*g'],
                ['b*a + x*b', 'g*b + x*x']]
        res2 = [['a*b + d*g', 'a*b + b*g'],
                ['b*b + d*x', 'b*b + x*b']]

        A = SymArray(a)
        B = SymArray(b)
        Res1 = SymArray(res1)
        Res2 = SymArray(res2)

        self.assertEqual(A*A, Res1)
        self.assertEqual(A*B, Res2)

    def test_arra_length(self):
        A = SymArray(self.a)
        self.assertEqual(A.size[0], len(A))
        self.assertEqual(A.size[0], 4)
        self.assertEqual(A.size[1], len(A[0]))
        self.assertEqual(A.size[1], 4)

    def test_row_change(self):
        res1 = [['a*a + b*g', 'a*g + x*g'],
                ['b*a + x*b', 'g*b + x*x']]
        array =  SymArray(A)
        switch_Rows

if __name__ == '__main__':
    unittest.main()
