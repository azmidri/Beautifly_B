
import unittest
import BrushingDataframe as bdf
import pandas as pd
import numpy as np
import io
import sys
sample_df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                   'num_wings': [2, 0, 0, 0],
                   'num_specimen_seen': [10, 2, 1, 8]})
sample_array = pd.array([1, 2])
empty_df = pd.DataFrame()

types_df = pd.DataFrame({'num_legs': [2, 0, 'bayan', 0],
                   'num_wings': [2, 0, 0, 0],
                   'num_specimen_seen': [10, 'bayan', 1, 8],
                   'name':['teamB','teamA','teamB','bayan']})
sample_myrdf = bdf.BrushingDataframe(sample_df)
sample_myarray = bdf.BrushingDataframe(sample_array)
empty_myrdf = bdf.BrushingDataframe(empty_df)

types_myrdf = bdf.BrushingDataframe(types_df)
class TestScanning(unittest.TestCase):
    def test_setatt_type(self):
        #check if setAttributes method handles unidentified types 
        capturedOutput = io.StringIO()                  
        sys.stdout = capturedOutput                     
        sample_myrdf.SetAttributes({'num_legs':'nonint','num_wings':'nonint','num_specimen_seen':'float'})   
        sys.stdout = sys.__stdout__                     
        captured = capturedOutput.getvalue() 
        self.assertTrue("undefined type" in captured.lower())
    def test_setatt_invaliddata(self):
        #check if setAttributes method handles invalid data in the dataframe 
        capturedOutput = io.StringIO()                  
        sys.stdout = capturedOutput                     
        types_myrdf.SetAttributes({'num_legs':'int'})   
        sys.stdout = sys.__stdout__                     
        captured = capturedOutput.getvalue() 
        self.assertIn("contains invalid values",captured.lower())
    def test_setatt_missingdata(self):
        #check if setAttributes method handles missing data in the dataframe  
        missings_df = pd.DataFrame({'num_legs': [2, 0, np.NaN, 0],
                   'num_wings': [2, 0, 0, 0],
                   'num_specimen_seen': [10, None, 1, 8],
                   'name':['teamB','teamA','teamB',None]}) 
        missing_myrdf = bdf.BrushingDataframe(missings_df)    
        missing_myrdf.SetAttributes({'num_legs':'int','num_wings':'int','num_specimen_seen':'float'})  
    def test_setatt_vars(self):
        #check if setAttributes method handles unidentified column names 
        capturedOutput = io.StringIO()                  
        sys.stdout = capturedOutput                     
        sample_myrdf.SetAttributes({'legs':'int','num_wings':'int','num_specimen_seen':'float'})   
        sys.stdout = sys.__stdout__                     
        captured = capturedOutput.getvalue()   
        self.assertTrue("does not contain variable" in captured.lower())
    def test_setatt_empty(self):
        #check if setAttributes method handles empty dataframes 
        capturedOutput = io.StringIO()                  
        sys.stdout = capturedOutput                     
        empty_myrdf.SetAttributes({'legs':'int','num_wings':'int','num_specimen_seen':'float'})   
        sys.stdout = sys.__stdout__                     
        captured = capturedOutput.getvalue()   
        self.assertTrue("the dataframe has not yet been initialized" in captured.lower())
    def test_cleaning_missing(self):
        #check if cleaning missing method is able to correctly use median/mode for filling missing data. 
        missings_df = pd.DataFrame({'num_legs': [2, 0, np.NaN, 0],
                   'num_wings': [2, 0, 0, 0],
                   'num_specimen_seen': [10, None, 1, 8],
                   'name':['teamB','teamA','teamB',None]}) 
        missing_myrdf = bdf.BrushingDataframe(missings_df)
        missing_myrdf.cleaning_missing()
        self.assertAlmostEqual(missing_myrdf['num_legs'][2],0.0)
        self.assertAlmostEqual(missing_myrdf['num_specimen_seen'][1],8.0)
        self.assertIn(missing_myrdf['name'][3].lower(),'teamb')
    def test_cleaning_missing_array(self):
        self.assertAlmostEqual(sample_myarray.cleaning_missing()[0][0],1.0)
    def test_cleaning_missing_empty(self):
        empty_myrdf.cleaning_missing()
    def test_scanning(self):
        sample_df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                   'num_wings': [2, 0, 0, 0],
                   'num_specimen_seen': [10, 2, 1, 8]})
        sample_myrdf = bdf.BrushingDataframe(sample_df)
        capturedOutput = io.StringIO()                  
        sys.stdout = capturedOutput    
        sample_myrdf.scanning()
        sys.stdout = sys.__stdout__                     
        captured = capturedOutput.getvalue()   
        self.assertTrue("data scan and visualization is reported under beutifly_b eda.html." in captured.lower())