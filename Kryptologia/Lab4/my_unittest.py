from stream_key import LinearFeedbackShiftRegister
import unittest


class UnitTest(unittest.TestCase):
    # def test_LFSR(self):
    #     reg1 = LinearFeedbackShiftRegister(config=5, init_state=10)
        # reg1 = LinearFeedbackShiftRegister(config=0b111, init_state=10)

    def test_next_step(self):
        reg1 = LinearFeedbackShiftRegister(config=0, init_state=4)
        reg1.next_step()
        self.assertEqual(9, reg1.state)
        reg1.next_step()
        self.assertEqual(19, reg1.state)

        reg1 = LinearFeedbackShiftRegister(config=0, init_state=0)

        reg1.next_step()
        self.assertEqual(1, reg1.state)

        reg1.next_step()
        self.assertEqual(3, reg1.state)

    def test_parameters(self):
        reg1 = LinearFeedbackShiftRegister(config=0, init_state=255)
        self.assertEqual(255, reg1._max_num)
        self.assertEqual(255, reg1.state)
        self.assertEqual(None, reg1.last_bit)

        reg1 = LinearFeedbackShiftRegister(config=0, init_state=256)
        self.assertEqual(0, reg1.state)

        reg1 = LinearFeedbackShiftRegister(config=0, init_state=260)
        self.assertEqual(4, reg1.state)

    def test_next_step_config_biger(self):
        reg1 = LinearFeedbackShiftRegister(config=73, init_state=4)
        reg1.next_step()

    def test_next_step_overflow(self):
        reg1 = LinearFeedbackShiftRegister(config=0, init_state=256)
        
        reg1.next_step()
        self.assertEqual(1, reg1.state)
        self.assertEqual(0, reg1.last_bit)

        reg1.next_step()
        self.assertEqual(3, reg1.state)
        self.assertEqual(0, reg1.last_bit)

    def test_next_step_lastbit(self):
        reg2 = LinearFeedbackShiftRegister(config=0, init_state=143)
        
        reg2.next_step()        
        self.assertEqual(1, reg2.last_bit)

        reg2.next_step()
        reg2.next_step()
        self.assertEqual(0, reg2.last_bit)

        reg2.next_step()
        self.assertEqual(0, reg2.last_bit)

        reg2.next_step()
        self.assertEqual(1, reg2.last_bit)

    def test_next_step_config_1(self):
        reg1 = LinearFeedbackShiftRegister(config=1, init_state=13)

        reg1.next_step()
        self.assertEqual(26, reg1.state)

        reg1.next_step()
        self.assertEqual(53, reg1.state)

    def test_next_step_config_2(self):
        reg2 = LinearFeedbackShiftRegister(config=5, init_state=13)

        reg2.next_step()
        self.assertEqual(27, reg2.state)

        reg2.next_step()
        self.assertEqual(54, reg2.state)

    def test_next_step_config_3(self):
        reg3 = LinearFeedbackShiftRegister(config=21, init_state=8)

        reg3.next_step()
        self.assertEqual(17, reg3.state)

        reg3.next_step()
        self.assertEqual(35, reg3.state)


unittest.main()
