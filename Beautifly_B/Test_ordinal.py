import unittest
import pandas as pd
import numpy as np
from ordinal import Ordinal

df = pd.DataFrame({'country': ['france', 'spain', 'france', 'france','spain','france'],
'rank':[1,1,1,2,2,1]})
column = 'rank'
new_ord = column+"_ORD"
sample_1 = pd.DataFrame({'country': ['france', 'spain', 'france', 'france','spain','france'],
'rank':[1,1,1,None,2,1]})
class TestWOE(unittest.TestCase):
    def test_basic_ordinal(self):
        df[new_ord] = np.vectorize(Ordinal.make_ordinal)(df[column].values)   
        self.assertEqual(df[new_ord][0],'1st')
    def test_missing_ordinal(self):
        sample_1[new_ord] = np.vectorize(Ordinal.make_ordinal)(sample_1[column].values)   
        self.assertEqual(sample_1[new_ord][0],'1st')

        #self.assertRaises(ValueError,Ordinal.make_ordinal,sample_1[column].values)
    def test_one_number(self):
        self.assertEqual(Ordinal.make_ordinal(1),'1st')
        self.assertEqual(Ordinal.make_ordinal(2),'2nd')
        self.assertEqual(Ordinal.make_ordinal(3),'3rd')
        self.assertEqual(Ordinal.make_ordinal(4),'4th')
        self.assertEqual(Ordinal.make_ordinal(21),'21st')
