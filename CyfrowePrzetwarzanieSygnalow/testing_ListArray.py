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
        ar0 = [['a*a + b*g', 'a*g + x*g'],
               ['b*a + x*b', 'g*b + x*x']]
        ar1_a = [['a*a + b*g', 'a*g + x*g'],
                 ['a*a + b*g', 'a*g + x*g']]
        ar1_b = [['b*a + x*b', 'g*b + x*x'],
                 ['b*a + x*b', 'g*b + x*x']]
        ar1_c = [['b*a + x*b', 'g*b + x*x'],
                 ['a*a + b*g', 'a*g + x*g']]

        array0 = SymArray(ar0)
        new_array_a = array0.switch_rows([0, 0])
        new_array_b = array0.switch_rows([1, 1])
        new_array_c = array0.switch_rows([1, 0])

        self.assertEqual(new_array_a, SymArray(ar1_a))
        self.assertEqual(new_array_b, SymArray(ar1_b))
        self.assertEqual(new_array_c, SymArray(ar1_c))

    def test_row_change(self):
        ar0 = [['a', 'b', 'c'],
               ['a', 'd', 'g']]
        ar1_a = [['a', 'a', 'a'],
                 ['a', 'a', 'a']]
        ar1_b = [['b', 'b', 'b'],
                 ['d', 'd', 'd']]
        ar1_c = [['c', 'b', 'a'],
                 ['g', 'd', 'a']]

        array0 = SymArray(ar0)
        new_array_a = array0.switch_cols([0, 0, 0])
        new_array_b = array0.switch_cols([1, 1, 1])
        new_array_c = array0.switch_cols([2, 1, 0])

        self.assertEqual(new_array_a, SymArray(ar1_a))
        self.assertEqual(new_array_b, SymArray(ar1_b))
        self.assertEqual(new_array_c, SymArray(ar1_c))

    def test_1d_rows_cols_swtich(self):
        pass
        
    def test_rowcols_change(self):
        ar0 = [['a', 'b', 'c'],
               ['a', 'd', 'g'],
               ['b', 'd', 'f']]
        ar1_a = [['a', 'a', 'a'],
                 ['a', 'a', 'a'],
                 ['a', 'a', 'a']]
        ar1_b = [['d', 'b', 'f'],
                 ['d', 'a', 'g'],
                 ['b', 'a', 'c']]

        array0 = SymArray(ar0)  # initial array for operations

        # Checking with ar1_a
        new_array_a = array0.switch_cols([0, 0, 0])
        new_array_a = new_array_a.switch_rows([1, 1, 1])
        self.assertEqual(new_array_a, SymArray(ar1_a))
        # Checking with ar1_b
        new_array_b = array0.switch_rows([2, 1, 0])
        new_array_b = new_array_b.switch_cols([1, 0, 2])
        self.assertEqual(new_array_b, SymArray(ar1_b))


if __name__ == '__main__':
    unittest.main()
