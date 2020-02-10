# Predicting House Prices in Kings County, Seattle

Project members: Finn and Thomas

Executive Summary:
Creating value for money using in depth data analysis technics to ensure detailed information on the properties and their potential for future improvement.

Using the data available, we were able to established the top 6 features in influencing house prices
We were able also able to establish that waterfront properties attract higher prices (common sense) alongside the breakdown of prices according to the above features.
Also managed to find a trend over the data time period suggesting that higher number of transaction have an average impact on prices and vice versa. 

We use our knowledge to give the latest market and property information using ,linear regression and multilinear regression to ensure as much detail as possible is captured.

High-level overview: 
Ahead of starting the project, managed to laid down 3 questions to be answered including
	1. What are the top 6 house features that are the most important in determining house prices
	2. How much in avg. is the price difference between waterfront houses and non-waterfront houses
	3. How have avg. house prices faired the last 12 months and when is the best time of the year to sell?
	4. [Bonus] Identify the avg. price and transactions per zipcode. Determine if there's any relationship between them
Pre analysis, executed data cleaning including removing duplicates, filling null values, changing data types, checking and removing outliers as well as some simple form of feature engineering. Subsequently proceed to execute some basic data visualisation and EDA.

Question 1 was solved using a combination of using a correlation matrix, simple and multiple linear regression. Whilst obtaining a 70% R2 for the multiple model, there remains several pitfalls (explained in the notebook) which might suggest linear regression may not be the ideal model.

Question 2,3 and 4 were basically solved through some data manipulation through panda groupby methods as well as an extensive use of visualisation packages. One issue encountered was the different methods of visualising data and hence can be fairly confusing and time consuming at times.


Task delegation:
Contributed to different parts of codes and presentation according to individuals' strengths

We hope you will find some insightful details in this notebook and will be happy to answer any questions you might have. Thank you.
