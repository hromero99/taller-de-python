from models import Mueble
import unittest


class MesaConstructor(unittest.TestCase):

    def test_default_args(self):
        mueble_1 = Mueble()
        self.assertEqual(mueble_1.id, 0)
    def test_args(self):
        mueble_1 = Mueble(nombre="mesa")
        self.assertEqual(mueble_1.name, 'mesa')

if __name__ == '__main__':
    unittest.main()
