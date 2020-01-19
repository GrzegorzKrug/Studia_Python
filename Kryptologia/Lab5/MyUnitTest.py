from BitCoin import TimeServer, BitCoin, Miner
import unittest


class MyTimeServer(unittest.TestCase):
    def test_time1(self):
        serv1 = TimeServer()
        time0 = serv1.time()
        self.assertEqual(type(time0), int)

    def test_time2(self):
        serv1 = TimeServer()
        time0 = serv1.time_str()
        self.assertEqual(type(time0), str)


class BitTest(unittest.TestCase):
    def test_bit1(self):
        test_string = 'asdasdasdacvxweqr324'
        abc = BitCoin()

        abc.find_hash(test_string, 5)


if __name__ == "__main__":
    unittest.main()
