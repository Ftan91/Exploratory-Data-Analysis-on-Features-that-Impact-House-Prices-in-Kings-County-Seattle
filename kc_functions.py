import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.stats.api as sms
from statsmodels.formula.api import ols

def datatype_search(dataframe, column):
    """This function returns number of unique datatype as well as lists out all datatypes in a particular column"""
    
    x = dataframe[column].unique()
    y = set([type(number) for number in x])
    z = len(y)
    
    return list(y), z

def data_quality_summary(data):
    """This function returns a dataframe which summarises potential data quality issues for each column"""        
    
    dictionary = {'Feature': [],
                 'Null Entries': [],
                 'No. of unique datatype(s)' : [],
                 'Feature datatype(s)' : [],
                 'Min, Max': []
                 }
    
    for column in data.columns:
        dictionary['Feature'].append(column)
        dictionary['Null Entries'].append(data[column].isnull().sum())
        dictionary['No. of unique datatype(s)'].append(datatype_search(data, column)[1])
        dictionary['Feature datatype(s)'].append(datatype_search(data, column)[0])
        dictionary['Min, Max'].append((data[column].min(), data[column].max()))
        
    summary = pd.DataFrame(dictionary)
    
    return summary

def null_filler(data, column):
    """This function fills in empty cells using unique values in the particular column according to its existing weight"""
    
    if column == 'sqft_basement':
        basement_unique = data[data['sqft_basement'] != '?']['sqft_basement'].unique()
        basement_prob = data[data['sqft_basement'] != '?']['sqft_basement'].value_counts(normalize = True)
        return np.random.choice(basement_unique, 1, p= basement_prob)[0]
    
    else:
        unique = data[data[column].notnull()][column].unique()
        prob = data[data[column].notnull()][column].value_counts(normalize = True)
        return np.random.choice(unique, 1, p= prob)[0]

def year_value(row):
    """This function replaces 0 value in the 'yr_renovated' column with the yr_built value"""
    
    if row["yr_renovated"] == 0.0 or pd.isna(row["yr_renovated"]) == True:
        return row["yr_built"]
    else:
        return row["yr_renovated"]

def OLS_summary(feature_correlations, data, scale):
    """This function returns a summary table of conducted regression analysis"""
    
    summary = {'feature' : [], 
           'Pearson_r'  : [], 
           'Pearson_r2' : [], 
           'R2' : [], 
           'P_value': [],
           'Coef_value' : [],
            'Coef_interval' : [],
           'F_value' : [],
           'T_value' : [],
            'Jacque-Bera' : [],
           'Resid. Skew': [],
           'Resid. Kurtosis': []
          }

    if scale == 'normal':    
        for index in range(len(feature_correlations)):
            f = 'price~' + feature_correlations.index[index]
            model = ols(formula = f, data = data).fit()
            summary['feature'].append(feature_correlations.index[index])
            summary['Pearson_r'].append(round(feature_correlations[index],2))
            summary['Pearson_r2'].append(round(feature_correlations[index] ** 2,2))
            summary['R2'].append(round(model.rsquared,2))
            summary['P_value'].append(round(model.pvalues[1],2))
            summary['F_value'].append(round(model.fvalue,2))
            summary['T_value'].append(round(model.tvalues[1],2))
            summary['Resid. Skew'].append(round(sms.jarque_bera(model.resid)[2],2))
            summary['Resid. Kurtosis'].append(round(sms.jarque_bera(model.resid)[-1],2))
            summary['Jacque-Bera'].append(round(sms.jarque_bera(model.resid)[0],2))
            summary['Coef_value'].append(round(model.params[1],2))
            x = model.conf_int(alpha = 0.05, cols = None)
            y = [round(x.loc[feature_correlations.index[index], 0],2), round(x.loc[feature_correlations.index[index], 1],2)]
            summary['Coef_interval'].append(y)
        summary_df = pd.DataFrame(summary)
        return summary_df
    elif scale == 'log':
        for index in range(len(feature_correlations)):
            f = 'price_log~' + feature_correlations.index[index]
            model = ols(formula = f, data = data).fit()
            summary['feature'].append(feature_correlations.index[index])
            summary['Pearson_r'].append(round(feature_correlations[index],2))
            summary['Pearson_r2'].append(round(feature_correlations[index] ** 2,2))
            summary['R2'].append(round(model.rsquared,2))
            summary['P_value'].append(round(model.pvalues[1],2))
            summary['F_value'].append(round(model.fvalue,2))
            summary['T_value'].append(round(model.tvalues[1],2))
            summary['Resid. Skew'].append(round(sms.jarque_bera(model.resid)[2],2))
            summary['Resid. Kurtosis'].append(round(sms.jarque_bera(model.resid)[-1],2))
            summary['Jacque-Bera'].append(round(sms.jarque_bera(model.resid)[0],2))
            summary['Coef_value'].append(round(model.params[1],2))
            x = model.conf_int(alpha = 0.05, cols = None)
            y = [round(x.loc[feature_correlations.index[index], 0],2), round(x.loc[feature_correlations.index[index], 1],2)]
            summary['Coef_interval'].append(y)
        summary_df = pd.DataFrame(summary)
        return summary_df
    else:
        for index in range(len(feature_correlations)):
            f = 'price_minmax~' + feature_correlations.index[index]
            model = ols(formula = f, data = data).fit()
            summary['feature'].append(feature_correlations.index[index])
            summary['Pearson_r'].append(round(feature_correlations[index],2))
            summary['Pearson_r2'].append(round(feature_correlations[index] ** 2,2))
            summary['R2'].append(round(model.rsquared,2))
            summary['P_value'].append(round(model.pvalues[1],2))
            summary['F_value'].append(round(model.fvalue,2))
            summary['T_value'].append(round(model.tvalues[1],2))
            summary['Resid. Skew'].append(round(sms.jarque_bera(model.resid)[2],2))
            summary['Resid. Kurtosis'].append(round(sms.jarque_bera(model.resid)[-1],2))
            summary['Jacque-Bera'].append(round(sms.jarque_bera(model.resid)[0],2))
            summary['Coef_value'].append(round(model.params[1],2))
            x = model.conf_int(alpha = 0.05, cols = None)
            y = [round(x.loc[feature_correlations.index[index], 0],2), round(x.loc[feature_correlations.index[index], 1],2)]
            summary['Coef_interval'].append(y)
        summary_df = pd.DataFrame(summary)
        return summary_df