# Predicting House Prices in Kings County, Seattle

Executive Summary:

The Kings County dataset contains house sale prices for Kings County in Seattle. It includes homes sold between May 2014 and May 2015. Alongside sale price, dataset also contains various attributes of each house sold such as number of rooms, square foot and location.

This notebooks aims to answer the below questions:
    1. What are the top 6 house features that are the most important in determining house prices
    2. How much in average is the price difference between waterfront houses and non-waterfront houses
    3. How have average house prices faired the last 12 months and when is the best time of the year to sell?
    4. Identify the average price and average transactions per zipcode. Determine if there's any relationship between them
    
Pre-analysis, executed data cleaning including removing duplicates, filling null values, changing data types, checking and removing outliers as well as some simple form of feature engineering. Subsequently proceeded to execute some basic data visualisation and EDA. Post data-cleaning and EDA, I applied a basic simple and multiple regression analysis to determine if there are any meaningful predictive house features that can be extracted.  

Question 1 was solved using a combination of using a correlation matrix, simple and multiple linear regression. Whilst obtaining a 70% R2 for the multiple regression model, there remains several pitfalls (explained in the notebook) which might suggest linear regression may not be the ideal model.

Question 2, 3 and 4 were basically solved through some data manipulation through panda groupby methods as well as an extensive use of visualisation packages. One issue encountered was the different methods of visualising data and hence can be fairly confusing and time consuming at times.

We hope you will find some insightful details in this notebook and will be happy to answer any questions you might have. Thank you.
