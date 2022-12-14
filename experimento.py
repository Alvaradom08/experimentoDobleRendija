import unittest
from DobleRendija import *
import math

class experimento(unittest.TestCase):
    def experimentoMultiple(self):
        mtrxDobleRendija = [
            [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
            [[1 / math.sqrt(2), 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
            [[1 / math.sqrt(2), 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
            [[0, 0], [-1 / math.sqrt(6), 1 / math.sqrt(6)], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
            [[0, 0], [-1 / math.sqrt(6), -1 / math.sqrt(6)], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0]],
            [[0, 0], [1 / math.sqrt(6), -1 / math.sqrt(6)], [-1 / math.sqrt(6), 1 / math.sqrt(6)], [0, 0], [0, 0],
             [1, 0], [0, 0], [0, 0]],
            [[0, 0], [0, 0], [-1 / math.sqrt(6), -1 / math.sqrt(6)], [0, 0], [0, 0], [0, 0], [1, 0], [0, 0]],
            [[0, 0], [0, 0], [1 / math.sqrt(6), -1 / math.sqrt(6)], [0, 0], [0, 0], [0, 0], [0, 0], [1, 0]]]

        estadoInicial = [[1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]

        self.assertEqual(experimentoMultiple(mtrxDobleRendija[:],estadoInicial[:], 2),
                         [[[0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0]],
                          [[0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0]],
                          [[0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0], [0.0, 0]],
                          [[0.1666666666666667, 0], [0.3333333333333334, 0], [0.0, 0], [1.0, 0], [0.0, 0], [0.0, 0],
                           [0.0, 0], [0.0, 0]],
                          [[0.1666666666666667, 0], [0.3333333333333334, 0], [0.0, 0], [0.0, 0], [1.0, 0], [0.0, 0],
                           [0.0, 0], [0.0, 0]],
                          [[0.0, 0], [0.3333333333333334, 0], [0.3333333333333334, 0], [0.0, 0], [0.0, 0], [1.0, 0],
                           [0.0, 0], [0.0, 0]],
                          [[0.1666666666666667, 0], [0.0, 0], [0.3333333333333334, 0], [0.0, 0], [0.0, 0], [0.0, 0],
                           [1.0, 0], [0.0, 0]],
                          [[0.1666666666666667, 0], [0.0, 0], [0.3333333333333334, 0], [0.0, 0], [0.0, 0], [0.0, 0],
                           [0.0, 0], [1.0, 0]]])

        rta = accionmatrizvector(experimentoMultiple(mtrxDobleRendija[:], estadoInicial[:], 2), estadoInicial)
        graficoProbabilidad(rta)
if __name__ == '__main__':
    unittest.main()