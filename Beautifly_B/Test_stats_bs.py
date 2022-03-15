import unittest
from stats_bs import Stats_BS
import pandas as pd
import numpy as np
import scipy.stats as stats
import math

df = pd.DataFrame({'column1': [1,2,4,5,67,8]})
sample_1 = pd.DataFrame({'column1': [1,2,4,None,67,8]})
sample_2 = pd.DataFrame({'column1': [1,-2,4,-5,67,8]})
sample_3 = pd.DataFrame({'column1': []})
sample_4 = pd.DataFrame()
kurt = 0
gmean = 0
skew = 0
class TestStats(unittest.TestCase):
    def test_basic_stats(self):
        kurt, gmean, skew  = Stats_BS.make_stats(df['column1'])
        self.assertAlmostEqual(round(kurt,3),1.135)
        self.assertAlmostEqual(round(gmean,3),5.271)
        self.assertAlmostEqual(round(skew,3),1.753)
    def test_missing_stats(self):
        kurt, gmean, skew  = Stats_BS.make_stats(sample_1['column1'])
        self.assertTrue(math.isnan(kurt))
        self.assertTrue(math.isnan(gmean))
        self.assertTrue(math.isnan(skew))
    def test_negative_stats(self):
        kurt, gmean, skew  = Stats_BS.make_stats(sample_2['column1'])
        self.assertAlmostEqual(round(kurt,3),1.003)
        self.assertTrue(math.isnan(gmean))
        self.assertAlmostEqual(round(skew,3),1.679)
    def test_empty_stats(self):
        kurt, gmean, skew  = Stats_BS.make_stats(sample_3['column1'])
        self.assertTrue(math.isnan(kurt))
        self.assertTrue(math.isnan(gmean))
        self.assertTrue(math.isnan(skew))