
import unittest
import BrushingDataframe as bdf
import pandas as pd
import io
import sys
sample_df = pd.DataFrame({'num_legs': [2, 4, 8, 0],
                   'num_wings': [2, 0, 0, 0],
                   'num_specimen_seen': [10, 2, 1, 8]})

sample_array = pd.array([1, 2])
empty_df = pd.DataFrame()
sample_myrdf = bdf.BrushingDataframe(sample_df)
sample_myarray = bdf.BrushingDataframe(sample_array)
empty_myrdf = bdf.BrushingDataframe(empty_df)
class TestScanning(unittest.TestCase):
    def test_setatt_type(self):
        #check if setAttributes method handles unidentified types 
        capturedOutput = io.StringIO()                  
        sys.stdout = capturedOutput                     
        sample_myrdf.SetAttributes({'num_legs':'nonint','num_wings':'int','num_specimen_seen':'float'})   
        sys.stdout = sys.__stdout__                     
        captured = capturedOutput.getvalue()   
        self.assertTrue("undefied type" in captured.lower())
    def test_setatt_vars(self):
        #check if setAttributes method handles unidentified variables 
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
