import unittest
from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np
from woe import WOE

sample_1 = pd.DataFrame({'country': ['france', 'spain', 'france', 'france','spain','france'],
'target':[1,1,1,0,0,1]})
sample_2 = pd.DataFrame({'country': ['france', 'spain', 'france', 'france','spain','france'],
'target':[1,0,1,1,0,1]})
sample_3 = pd.DataFrame({'country': ['france', 'spain', None, 'france','spain','france'],
'target':[1,1,1,0,0,1]})
sample_3a = pd.DataFrame({'country': ['france', 'spain', np.nan, 'france','spain','france'],
'target':[1,1,1,0,0,1]})
sample_4 = pd.DataFrame({'country': ['france', 'spain', 'france', 'france','spain','france'],
'target':[1,None,1,0,0,1]})
sample_4a = pd.DataFrame({'country': ['france', 'spain', 'france', 'france','spain','france'],
'target':[1,np.nan,1,0,0,1]})
sample_5 = pd.DataFrame()
sample_6 = pd.array([1, 2])
sample_7 = pd.DataFrame({'country': [1, 0, 1, 1,0,1],'target':[1,1,1,0,0,1]})
sample_8 = pd.DataFrame({'country': [2, 0, 2, 2,0,2],'target':[1,1,1,0,0,1]})
class TestWOE(unittest.TestCase):
    def test_basic_WOE(self):
        my_WOE = WOE()
        my_WOE.fit(sample_1,'country','target')
        sample_1.loc[:,'country'] = my_WOE.transform(sample_1,'country','target')
        self.assertAlmostEqual(round(sample_1.loc[:,'country'][0],6),0.405465)
    def test_allZero_WOE(self):
        my_WOE = WOE()
        my_WOE.fit(sample_2,'country','target')
        sample_2.loc[:,'country'] = my_WOE.transform(sample_2,'country','target')
        self.assertEqual(sample_2.loc[:,'country'][0],0)
    def test_missing_parameter_WOE_none(self):
        my_WOE = WOE()
        my_WOE.fit(sample_3,'country','target')
        sample_3.loc[:,'country'] = my_WOE.transform(sample_3,'country','target')
        self.assertEqual(round(sample_3.loc[:,'country'][0],6),0.287682)    
    def test_missing_parameter_WOE_nan(self):
        my_WOE = WOE()
        my_WOE.fit(sample_3a,'country','target')
        sample_3a.loc[:,'country'] = my_WOE.transform(sample_3a,'country','target')
        self.assertEqual(round(sample_3a.loc[:,'country'][0],6),0.287682)   
    def test_missing_target_WOE_none(self):
        my_WOE = WOE()
        my_WOE.fit(sample_4,'country','target')
        sample_4.loc[:,'country'] = my_WOE.transform(sample_4,'country','target')
        self.assertEqual(round(sample_4.loc[:,'country'][0],6),0.693147)  
    def test_missing_target_WOE_nan(self):
        my_WOE = WOE()
        my_WOE.fit(sample_4a,'country','target')
        sample_4a.loc[:,'country'] = my_WOE.transform(sample_4a,'country','target')
        self.assertEqual(round(sample_4a.loc[:,'country'][0],6),0.693147)  
    def test_fit_emptydf_WOE(self):
        my_WOE = WOE()
        self.assertRaises(ValueError,my_WOE.fit,sample_5,'country','target')
    def test_transform_emptydf_WOE(self):
        my_WOE = WOE()
        my_WOE.fit(sample_1,'country','target')
        self.assertRaises(ValueError,my_WOE.transform,sample_5,'country','target')
    def test_fit_type_WOE(self):
        my_WOE = WOE()
        self.assertRaises(TypeError,my_WOE.fit,sample_6,'country','target')
    def test_transform_type_WOE(self):
        my_WOE = WOE()
        my_WOE.fit(sample_1,'country','target')
        self.assertRaises(TypeError,my_WOE.transform,sample_6,'country','target')
    def test_numericInput_WOE(self):
        my_WOE = WOE()
        my_WOE.fit(sample_7,'country','target')
        sample_7.loc[:,'country'] = my_WOE.transform(sample_7,'country','target')
        self.assertAlmostEqual(round(sample_7.loc[:,'country'][0],6),0.405465)
    def test_numericInput2_WOE(self):
        my_WOE = WOE()
        my_WOE.fit(sample_8,'country','target')
        sample_8.loc[:,'country'] = my_WOE.transform(sample_8,'country','target')
        self.assertAlmostEqual(round(sample_8.loc[:,'country'][0],6),0.405465)