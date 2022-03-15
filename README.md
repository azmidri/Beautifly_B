# Beautifly_B
Beautifly_B is an open-source Python library that generates beautiful, high-density visualizations to kickstart EDA (Exploratory Data Analysis) with just Few lines of code. Output is a fully self-contained HTML application.

The system is built around quickly visualizing target values and comparing datasets. Its goal is to help quick analysis of target characteristics other such data characterization tasks.


...
"# Beautifly_B" 
_____________
Features
-----------------------------------------------------------------------------------------------------------------
- **Feature analysis** 
  - Shows features with Null Values 
  - Basic statistics like kurtosis, skewness and Gmean
  - Features Data Types with unique rows 
- **Visualize and compare**
  - Distinct datasets 
  - Intra-set characteristics (e.g. male versus female)
- **Mixed-type associations**
  - Beautifly_B integrates associations for numerical (Pearson's correlation), categorical (uncertainty coefficient) and categorical-numerical (correlation ratio) datatypes seamlessly, to provide maximum information for all data types.
- **Type inference**
  - Automatically detects numerical, categorical and text features, with optional manual overrides 
- **Summary information** 
  - Type, unique values, missing values, duplicate rows, most frequent values
  
-----------------------------------------------------------------------------------------------------------------
Upgrading 
-----------------------------------------------------------
Some people have experienced mixed results behavior upgrading through pip. To update to the latest from an existing install, it is recommended to pip uninstall Beautifly_B first, then simply install.

-----------------------------------------------------------------------------------------------------------------
Using pip
-----------------------------------------------------------------------------------------------------------------
The best way to install sweetviz (other than from source) is to use pip:

pip install Beautifly_B

-----------------------------------------------------------------------------------------------------------------

Basic Usage
-----------------------------------------------------------------------------------------------------------------
### cleaning_missing()
```
cleaning_missing(  self, input_vars=[])
```            
**cleaning_missing(...)** 
            The cleaning missing will identify the null values in the list passed to the function 
            and replaces values with median for the numerical features and Mode for the categorical feature
            
            Parameters
            ----------
            input_vars: list, default=Empty
            List of selected features. Default is empty where all columns will be included.
  
            Returns
            -------
            clean columns filled with missing values.
            
            Examples
             --------
            import pandas as pd
            import Beautifly_B.BrushingDataframe as bdf
            dataframe = pd.read_csv("AUTO_LOANS_DATA.csv", sep=";")
            dataframe['BINARIZED_TARGET'] = dataframe['BUCKET'].apply(lambda x: 1 if x>0 else 0)
            myrdf = bdf.BrushingDataframe(dataframe)
            myrdf.cleaning_missing()
          
### scanning()
```
scanning( self, input_vars=[])
```            
**scanning(...)**  
                   Scanning will scan each column, provides analysis, recommendation, statistics analysis, visualization 
                   of the histogram, bar plot and box plot to provide number of counts and distributions based on the features. 
                   In addition, correlation matrix is generated to provide pair wise correlation between each numerical feature. 
                   The recommendation check on suspected record ID features, data features and features with high number of 
                  Parameters
                  ----------
                  input_vars: list, default=Empty
                  List of selected features. Default is empty where all columns will be included.

                  Returns
                  -------
                  Beutifly_B EDA.html located in the same folder in of the notebook, message completion of the scanning and 
                  generating of the html report
                  
                  Examples
                  --------
                  import pandas as pd
                  import Beautifly_B.BrushingDataframe as bdf
                  dataframe = pd.read_csv("AUTO_LOANS_DATA.csv", sep=";")
                  dataframe['BINARIZED_TARGET'] = dataframe['BUCKET'].apply(lambda x: 1 if x>0 else 0)
                  myrdf = bdf.BrushingDataframe(dataframe)
                  myrdf.cleaning_missing()
                  myrdf.scanning()
          
### recommended_transformation()
```
recommended_transformation( self, input_vars=[],ordinal_vars=[], WOE_tresh = 10,  target='',reference_date= '',test_size_in= 0.3, WOE_print = False))
```            
**recommended_transformation(...)**  
                The recommended transformation provides several transformation and conversions that consist of 
                -	ordinal type conversion
                    Those features numerical features identified ordinal by user will be transformed 
                    to categorical such as 1st, 2nd and 3rd etc 
                -	date conversion to month    
                -	date conversion to number of days based on given reference date
                -	suspected record ID features removal
                -	categorical features transformation to numerical based on One hot encoding or Weight of Evidence 
                    (WOE) based on given threshold of number of categorical values.
                -	Standard scaler is selected by default.
    
                Parameters
                    ----------
                    input_vars: list, default=Empty
                    List of selected features. Default is empty where all columns will be included.
                     ordinal_vars: list, default=Empty
                     List of ordinal features. Default is empty where no column is included.
                     WOE_tresh: float or int, default=10
                     Weight of Evidence treshold of number of categorical features values that decides if categorical 
                     transformation is done with OneHotencoding or WOE. 
                     Examples: if WOE_tresh = 10, features with 10 unique category values will be transformed using OneHotEncoding,
                     whereas those with more than 10 will be under WOE
                     target: string, default = None
                     Target of the data sets that will be used for test , train splitting and and WO calculation
                     reference_date: string,default = None
                     The reference date is the name of the feature with type date that will be used for calculation 
                     of number of days against all other features with date format. 
                     test_size_in: float, default = 0.3
                     Tihs is the size of test data sets in percentage for the splitting between training and test. Beautifly_B will default
                     the splitting with stratify as the package is for classification binary only.
                     scaler: boolean, default True
                     Perform standard scaler if true
                    Returns
                    -------
                    X_train, X_test, y_train, y_test,  splittinglist, length=2 * len(arrays)
                    L List containing train-test split of inputs.
                    Feature_names  list of feature / column names of the dataframe
                    Examples
                    --------
                    import pandas as pd
                    import Beautifly_B.BrushingDataframe as bdf
                    dataframe = pd.read_csv("AUTO_LOANS_DATA.csv", sep=";")
                    dataframe['BINARIZED_TARGET'] = dataframe['BUCKET'].apply(lambda x: 1 if x>0 else 0)
                    myrdf = bdf.BrushingDataframe(dataframe)
                    myrdf.cleaning_missing()
                    myrdf.scanning() 
                    X_train, X_test, y_train, y_test, feature_names  = myrdf.recommended_transformation(ordinal_vars = ['ACCOUNT_NUMBER'],
                                                                                 WOE_tresh = 13,reference_date="CUSTOMER_OPEN_DATE",
                                                                              target = "BINARIZED_TARGET",scaler = True)
                    Important
                    The current version of Beautifly_B provides recommendation of data preparation for binary classification only.
                    More functionalities in the next release.
    
-----------------------------------------------------------------------------------------------------------------

References .
-----------------------------------------------------------------------------------------------------------------
Packages referenced are Holoviews, Bokeh and Hvplot.

-----------------------------------------------------------------------------------------------------------------

-----------------------------------------------------------------------------------------------------------------

Apply standard scaling for all input featuresit will provide a HTML page with the following: 
\\Features with Null Values
\\Features Basic Stats
\\Features data types
 \\In addition to different plots

