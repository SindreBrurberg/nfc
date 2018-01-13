import unittest
from button import Button

class TestButton(unittest.TestCase):

    def setUp(self):
        pass

    def test_button_propper_constrained_less_then_txt_len(self):
        b = Button("Screen", "LongString", "Funk", 0, 0, 6)
        self.assertEqual(b.propper(), False)

    def test_button_propper_constrained_grater_then_txt_len_and_extra(self):
        b = Button("Screen", "LongString", "Funk", 0, 0, 20)
        self.assertEqual(b.propper(), True)

    def test_button_propper_constrained_grater_then_txt_len_and_less_then_extra(self):
        b = Button("Screen", "LongString", "Funk", 0, 0, 12)
        self.assertEqual(b.propper(), False)

    def test_button_propper_unconstrained(self):
        b = Button("Screen", "LongString", "Funk", 0, 0)
        self.assertEqual(b.propper(), True)

    def test_button_nextpropper_constrained_less_then_txt_len(self):
        b = Button("Screen", "LongString", "Funk", 0, 0, 6)
        self.assertEqual(b.nextPropper(), 9)
        b = Button("Screen", "LongString", "Funk", 0, 1, 6)
        self.assertEqual(b.nextPropper(), 9)
        b = Button("Screen", "LongString", "Funk", 1, 0, 6)
        self.assertEqual(b.nextPropper(), 10)

    def test_button_nextpropper_constrained_less_then_min_len(self):
        b = Button("Screen", "LongString", "Funk", 0, 0, 3)
        self.assertEqual(b.nextPropper(), 9)
        b = Button("Screen", "LongString", "Funk", 0, 1, 3)
        self.assertEqual(b.nextPropper(), 9)
        b = Button("Screen", "LongString", "Funk", 1, 0, 3)
        self.assertEqual(b.nextPropper(), 10)

    def test_button_nextpropper_constrained_greater_then_txt_len(self):
        b = Button("Screen", "LongString", "Funk", 0, 0, 20)
        self.assertEqual(b.nextPropper(), 20)
        b = Button("Screen", "LongString", "Funk", 0, 1, 20)
        self.assertEqual(b.nextPropper(), 20)
        b = Button("Screen", "LongString", "Funk", 1, 0, 20)
        self.assertEqual(b.nextPropper(), 21)

    def test_button_nextpropper_unconstrained(self):
        b = Button("Screen", "LongString", "Funk", 0, 0)
        self.assertEqual(b.nextPropper(), 16)
        b = Button("Screen", "LongString", "Funk", 0, 1)
        self.assertEqual(b.nextPropper(), 16)
        b = Button("Screen", "LongString", "Funk", 1, 0)
        self.assertEqual(b.nextPropper(), 17)

    def test_button_under(self):
        b = Button("Screen", "LongString", "Funk", 0, 0)
        self.assertEqual(b.under(), 7)
        b = Button("Screen", "LongString", "Funk", 0, 1)
        self.assertEqual(b.under(), 8)
        b = Button("Screen", "LongString", "Funk", 1, 0)
        self.assertEqual(b.under(), 7)

    def test_button_under_no_bottom(self):
        b = Button("Screen", "LongString", "Funk", 0, 0, bottom = False)
        self.assertEqual(b.under(), 6)
        b = Button("Screen", "LongString", "Funk", 0, 1, bottom = False)
        self.assertEqual(b.under(), 7)
        b = Button("Screen", "LongString", "Funk", 1, 0, bottom = False)
        self.assertEqual(b.under(), 6)

    def test_width(self):
        b = Button("Screen", "LongString", "Funk", 1, 0)
        self.assertEqual(b.width(), 16)
        b.width(20)
        self.assertEqual(b.width(), 20)
        b.width(2)
        self.assertEqual(b.width(), 9)
        b.width(propper = True)
        self.assertEqual(b.width(), 16)
        b.width(2, True)
        self.assertEqual(b.width(), 16)

    def test_height(self):
        b = Button("Screen", "LongString", "Funk", 1, 0)
        self.assertEqual(b.height(), 7)
        b = Button("Screen", "LongString", "Funk", 1, 0, bottom = False)
        self.assertEqual(b.height(), 6)

if __name__ == '__main__':
    unittest.main()
