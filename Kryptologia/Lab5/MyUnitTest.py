from BitCoin import TimeServer
import unittest


class MyTest(unittest.TestCase):
    def test_time(self):
        serv1 = TimeServer()
        time0 = serv1.time()
        print(time0)
        self.assertEqual(type(time0), int)

    def test_time2(self):
        serv1 = TimeServer()
        time0 = serv1.time_str()
        print(time0)
        self.assertEqual(type(time0), str)


if __name__ == "__main__":
    unittest.main()
