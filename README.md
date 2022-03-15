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
**cleaning_missing(...)** scan each column, indicating if droping or keeping the variable for 
            modelling and why, for the ones keeping indicates which cleaning / transformation 
            is recommended for the missing values and if scalling / dummy creation is recommended, 
            if not always inform that is not necessary
            If column is Numerical variable the missing null values will be replaced with Mean
            If column is Categorical variable the missing null values will be replaced with Mode

        Returns
        -------
          clean columns filled with missing values.
          
### scanning()
```
scanning( self, input_vars=[])
```            
**scanning(...)**  provided Basic statistics like kurtosis, skewness and Gmean
                   Checks the data types
                   Plots histograms with variables 
                   Plots correlation between features

        Returns
        -------
          A print with the analysis or new clean columns .
          
### recommended_transformation()
```
recommended_transformation( self, input_vars=[],ordinal_vars=[], WOE_tresh = 10,  target='',reference_date= '',test_size_in= 0.3, WOE_print = False))
```            
**recommended_transformation(...)**  data preparation (for each column provide methods to perform
        transformations - for example: time calculation like age, days as customers, 
        days to due date, label encoding, imputation, standard scalling, dummy creation 
        or replacement of category value by its probability of default depending, justify 
        transformation depending of the variable type, or explain why transformation is 
        not necessary);

        Returns
        -------
          Print newly transformed columns .
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

